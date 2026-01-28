// Import THREE
import * as THREE from 'https://threejsfundamentals.org/threejs/resources/threejs/r132/build/three.module.js';
import { OrbitControls } from 'https://cdn.jsdelivr.net/npm/three@0.121.1/examples/jsm/controls/OrbitControls.js';

// Create Renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// Create Camera and Scene
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
camera.position.set(0, 0, 100);
const scene = new THREE.Scene();
const controls = new OrbitControls(camera, renderer.domElement);

// --------------------
// Shape Functions
// --------------------

// Point (0D Primitive)
function createPoint(position, color = 0xffff00, size = 5) {
  const geometry = new THREE.BufferGeometry().setFromPoints([position]);
  const material = new THREE.PointsMaterial({ color, size });
  return new THREE.Points(geometry, material);
}

// Line (1D Primitive)
function createLine(start, end, color = 0xffffff) {
  const geometry = new THREE.BufferGeometry().setFromPoints([start, end]);
  const material = new THREE.LineBasicMaterial({ color });
  return new THREE.Line(geometry, material);
}

// Quadratic Curve: y = 0.05x²

function createQuadraticCurve(a, b, c, xMin = -10, xMax = 10, segments = 50, color = 0xff0ff0) {
  const points = [];

  for (let i = 0; i <= segments; i++) {
    const x = THREE.MathUtils.lerp(xMin, xMax, i / segments);
    const y = a * x * x + b * x + c;
    points.push(new THREE.Vector3(x, y, 0));
  }

  const geometry = new THREE.BufferGeometry().setFromPoints(points);
  const material = new THREE.LineBasicMaterial({ color });
  return new THREE.Line(geometry, material);
}
// --------------------
// Create Shapes
// --------------------
// Line
const line1 = createLine(
  new THREE.Vector3(-20, -10, 0),
  new THREE.Vector3(20, -10, 0)
);
scene.add(line1);

const line2 = createLine(
  new THREE.Vector3(20, -10, 0),
  new THREE.Vector3(0, 10, 0)
);
scene.add(line2);

const line3 = createLine(
  new THREE.Vector3(0, 10, 0),
  new THREE.Vector3(-20, -10, 0)
);
scene.add(line3);

const line4 = createLine(
  new THREE.Vector3(0, 10, 0),
  new THREE.Vector3(-10, -15, 10)
);
scene.add(line4);

const line5 = createLine(
  new THREE.Vector3(-10, -15, 10),
  new THREE.Vector3(-20, -10, 0)
);
scene.add(line5);

const line6 = createLine(
  new THREE.Vector3(-10, -15, 10),
  new THREE.Vector3(20, -10, 0)
);
scene.add(line6);
// Render Loop
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();

