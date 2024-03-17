// An ArrayList is used to manage the list of Particles

class ParticleSystem {

  ArrayList<Particle> particles;    // An arraylist for all the particles
  PVector origin;                   // An origin point for where particles are birthed
  int size;
  int red;
  int blue;
  int green;

  ParticleSystem(int num, PVector v, int s, int r, int g, int b) {
    size = s;
    red = r;
    blue = b;
    green = g;
    particles = new ArrayList<Particle>();   // Initialize the arraylist
    origin = v.copy();                        // Store the origin point
    for (int i = 0; i < num; i++) {
      particles.add(new Particle(origin, size, red, green, blue));    // Add "num" amount of particles to the arraylist
    }
  }


  void run() {
    // Cycle through the ArrayList backwards, because we are deleting while iterating
    for (int i = particles.size()-1; i >= 0; i--) {
      Particle p = particles.get(i);
      p.run();
      //if (p.isDead()) {
      //  particles.remove(i);
      //}
    }
  }

  void addParticle(int a, PVector op) {
    Particle p;
    // Add either a Particle or CrazyParticle to the system
    if (a == 0) {
      PVector pos = new PVector(random(15, 640 - size), random(15, 480 - size));
      p = new Particle(pos, size, red, green, blue);
    } 
    else {
      //p = new CrazyParticle(origin);
      PVector pos = new PVector(op.x, op.y);
      p = new Particle(pos, size, red, green, blue);
    }
    particles.add(p);
  }

  void addParticle(Particle p) {
    particles.add(p);
  }

  // A method to test if the particle system still has particles
  boolean dead() {
    return particles.isEmpty();
  }
}
