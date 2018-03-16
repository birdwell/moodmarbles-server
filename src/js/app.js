import { WebGLRenderer, Scene, PerspectiveCamera, PointLight, SphereGeometry, Mesh, MeshPhongMaterial } from 'three';

import { updateParticles, createParticles } from './particles';
import { getRandomInt } from './utils';
import data from '../../data/coffee.json';

const app = () => {
	const WIDTH = window.innerWidth;
	const HEIGHT = window.innerHeight;

	const renderer = new WebGLRenderer({ antialias: true });

	renderer.setSize(WIDTH, HEIGHT);
	renderer.setClearColor(0x000000, 1);
	document.body.appendChild(renderer.domElement);

	const scene = new Scene();
	const camera = new PerspectiveCamera(50, WIDTH / HEIGHT);

	camera.position.z = 50;
	scene.add(camera);

	const particleSystem = createParticles();
	const spheres = [];

	const light = new PointLight(0xFFFFFF);
	light.position.set(-10, 15, 50);
	scene.add(light);

	const mood = {
		"sadness": 0xf1c40f,
		"joy": 0x3498db,
		"anger": 0xe74c3c
	};

	data.forEach((tweet, i) => {
		const sphereGeometry = new SphereGeometry(2, 10, 10);
		const phongMaterial = new MeshPhongMaterial({ color: mood[tweet.emotion] });
		const sphere = new Mesh(sphereGeometry, phongMaterial);
		
		sphere.position.x = getRandomInt(-50, 50);
		sphere.position.y = getRandomInt(-50, 50);
		sphere.rotation.set(0.4, 0.2, 0);
		
		spheres.push(sphere);
		scene.add(sphere);
	});

	scene.add(particleSystem);

	let t = 0;
	render();

	// Render the scene
	function render() {
		requestAnimationFrame(render);
		t += 0.03;
		spheres.forEach(s => {
			s.rotation.y += 0.01;
			s.position.z = -7 * Math.sin(t * 2);
		});
		updateParticles(particleSystem)
		renderer.render(scene, camera)
	}
};

export default app;
