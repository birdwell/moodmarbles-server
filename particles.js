function createParticles() {
    var particleCount = 1800;
    var particles = new THREE.Geometry();
    var texture = new THREE.TextureLoader().load("images/particle.png")
    var pMaterial = new THREE.PointsMaterial({
        map: texture,
        transparent: true,
        opacity: 1.0,
        size: 10
    });
    for (var p = 0; p < particleCount; p++) {
        var pX = Math.random() * 500 - 250;
        var pY = Math.random() * 500 - 250;
        var pZ = Math.random() * 500 - 250;
        var particle = new THREE.Vector3(pX, pY, pZ);
        particle.velocity = new THREE.Vector3(0, -Math.random(), 0);
        particles.vertices.push(particle);
    }
    var particleSystem = new THREE.Points(
        particles, 
        pMaterial);
    
    //particleSystem.sortParticles = true;

    return particleSystem;
}

function updateParticles(particleSystem) {
    particleSystem.rotation.y += 0.01;
}