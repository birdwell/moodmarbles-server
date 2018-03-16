import { Geometry, TextureLoader, PointsMaterial, Vector3, Points } from 'three';
import particleImage from '../images/particle.png';
export const createParticles = () => {
    const particleCount = 1800;
    const particles = new Geometry();
    const texture = new TextureLoader().load(particleImage, () => { }, () => { }, (err) => console.error(err));
    const pMaterial = new PointsMaterial({
        map: texture,
        transparent: true,
        opacity: 1.0,
        size: 10
    });

    for (let p = 0; p < particleCount; p++) {
        const pX = Math.random() * 500 - 250;
        const pY = Math.random() * 500 - 250;
        const pZ = Math.random() * 500 - 250;
        const particle = new Vector3(pX, pY, pZ);
        
        particle.velocity = new Vector3(0, -Math.random(), 0);
        particles.vertices.push(particle);
    }

    return new Points(particles, pMaterial);
}

export const updateParticles = (particleSystem) => {
    particleSystem.rotation.y += 0.01;
}