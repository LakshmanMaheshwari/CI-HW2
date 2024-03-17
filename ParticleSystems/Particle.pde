// A simple Particle class

class Particle {
  PVector position;
  PVector velocity;
  PVector acceleration;
  float lifespan;
  int red;
  int blue;
  int green;
  int size;

  Particle(PVector l, int s, int r, int g, int b) {
    acceleration = new PVector(0, 0.05);
    velocity = new PVector(random(-1, 1), random(-1, 1));
    //velocity = new PVector(1, 1);
    position = l.copy();
    lifespan = 255.0;
    size = s;
    red = r;
    green = g;
    blue = b;
    
  }

  void run() {
    if (size == 8){
      update();  
    }
    display();
  }

  // Method to update position
  void update() {
    //velocity.add(acceleration);
    position.add(velocity);
    //lifespan -= 2.0;
  }

  // Method to display
  void display() {
    stroke(255, lifespan);
    fill(red, green, blue, lifespan);
    ellipse(position.x, position.y, size, size);
  }

  // Is the particle still useful?
  boolean isDead() {
    return (lifespan < 0.0);
  }
}
