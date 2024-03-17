/**
 * Multiple Particle Systems
 * by Daniel Shiffman.
 *
 * Click the mouse to generate a burst of particles
 * at mouse position.
 *
 * Each burst is one instance of a particle system
 * with Particles and CrazyParticles (a subclass of Particle). 
 * Note use of Inheritance and Polymorphism.
 
 */

ParticleSystem nucleus;
ParticleSystem electrons;
int count = 0;
boolean nucleus_done = false;
boolean start = true;
boolean electron_time = false;
int nucleus_limit = 200;
void setup() {
  size(640, 480);
  //systems = new ArrayList<ParticleSystem>();
}

void draw() {
  background(0);
  if (count <= nucleus_limit && !start){
    PVector a = new PVector(1,2);
    nucleus.addParticle(0, a);
  }
  else if (count > nucleus_limit && count < nucleus_limit + 2 && electron_time && !start){
    PVector a = new PVector(1,2);
    electrons.addParticle(0, a);
  }
  
  
  if (!start){
    count = count + 1;
    nucleus.run();
  }
  if (electron_time){
    for (Particle ns: nucleus.particles){
      boolean adde = false;
      for (Particle es: electrons.particles){
        float d = pow(pow(es.position.x - ns.position.x, 2) + pow(es.position.y - ns.position.y, 2), 0.5); 
        if (d < nucleus.size/2 + electrons.size/2){
          es.lifespan = 0;
          adde = true;  
          break;
        }
      }
      if (adde){
        PVector tp = ns.position;
        electrons.addParticle(1, tp);
      }
    }
    electrons.run();
  }
    
    
  if (start) {
    fill(255);
    textAlign(CENTER);
    text("click mouse to add nuclei", width/2, height/2);
  }
}

void mousePressed(){
  if (start){
    start = false;
  }
  if (!nucleus_done){
    //systems.add(new ParticleSystem(1, new PVector(mouseX, mouseY), 15, 128, 128, 0));
    nucleus = new ParticleSystem(1, new PVector(mouseX, mouseY), 15, 128, 128, 0);
    nucleus_done = true;
  }
  else if (!electron_time){
    electron_time = true;
    electrons = new ParticleSystem(1, new PVector(mouseX, mouseY), 8, 255, 165, 0);
  }
}

void reset(){
  count = 0;
  nucleus_done = false;
  start = true;
  electron_time = false; 
}

void keyPressed(){
  if (key == 'r' || key == 'R'){
    reset();
  }
  if (key == 'n' || key == 'N'){
    nucleus_limit++; 
  }
  if (key == 'm' || key == 'M'){
    nucleus_limit--; 
  }
}
