const createArtifacts = () => {
    const body = document.body;
    for (let i = 0; i < 5; i++) {
        const circle = document.createElement('div');
        circle.className = 'artifact artifact-circle';
        circle.style.top = Math.random() * 100 + 'vh'; // Random vertical position
        circle.style.left = Math.random() * 100 + 'vw'; // Random horizontal position
        body.appendChild(circle);

        const rectangle = document.createElement('div');
        rectangle.className = 'artifact artifact-rectangle';
        rectangle.style.top = Math.random() * 100 + 'vh'; // Random vertical position
        rectangle.style.left = Math.random() * 100 + 'vw'; // Random horizontal position
        body.appendChild(rectangle);

        const triangle = document.createElement('div');
        triangle.className = 'artifact artifact-triangle';
        triangle.style.top = Math.random() * 100 + 'vh'; // Random vertical position
        triangle.style.left = Math.random() * 100 + 'vw'; // Random horizontal position
        body.appendChild(triangle);
    }
};

document.addEventListener('DOMContentLoaded', createArtifacts);
