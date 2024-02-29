#include <iostream>
#include <string>
#include <windows.h>

/*
srand(time(NULL));  int answer = std::rand() % 5;  std::cout << answer  << "\n";

[ENDING OPTION 1: Confrontation with the Dark Crack Sorcerer]

[INT. DARK SORCERER'S LAIR - NIGHT]

You and Mozz cautiously navigate through the dark, twisting corridors of the sorcerer's lair, the air thick with the stench of dark magic. As you delve deeper, you can feel the oppressive weight of the sorcerer's power pressing down on you.

Suddenly, you come face to face with the Dark Crack Sorcerer himself, a menacing figure cloaked in shadows. His eyes gleam with malevolence as he raises his staff, ready to unleash his dark magic upon you.

DARK SORCERER: Foolish mortals! You dare to challenge me?

With bravery in your hearts, you and Mozz stand firm, ready to face the sorcerer head-on. A fierce battle ensues, magic crackling through the air as you clash with the forces of darkness.

[ENDING 1: Victory]

With determination and skill, you and Mozz manage to overpower the Dark Crack Sorcerer, breaking his hold over Sunderland and bringing an end to his reign of terror. The city is saved, and you emerge as heroes, hailed by the people for your bravery and selflessness.

[ENDING 2: Defeat]

Despite your best efforts, the Dark Crack Sorcerer proves to be too powerful, overwhelming you and Mozz with his dark magic. As you lie defeated, the sorcerer's laughter echoes through the chamber, signaling the doom of Sunderland and the triumph of darkness.

[ENDING 3: Sacrifice]

Realizing that defeating the Dark Crack Sorcerer may require a sacrifice, you and Mozz make the ultimate decision to channel all your remaining strength and magic into a final, desperate attack. With a blinding flash of light, you unleash a devastating blast that consumes both you and the sorcerer, sacrificing yourselves to save Sunderland from destruction. Though you may be gone, your sacrifice ensures that the city will live on, free from the darkness that once threatened to consume it.



*/
//Forest function for mid path
int forest(std::string location, std::string nextpage) {

  std::cout << " \n"; std::cout << " \n";
  std::cout << "INT. MYSTERIOUS FOREST - DAY";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "You and Mozz find yourselves deep in the heart of the " << location << " forest. \n";
  std::cout << "The ancient trees tower above you, their gnarled branches reaching out like skeletal fingers. \n";
  std::cout << "Sunlight filters through the dense canopy, casting intricate patterns of light and shadow on the forest floor.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "MOZZ: (whispering) This forest feels... alive.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "YOU: (nodding) I know what you mean. It's like it's watching us.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "As you venture deeper into the forest, you can't shake the feeling of being watched. \n";
  std::cout << "Strange whispers seem to echo through the trees, and the rustling of leaves sends shivers down your spine. \n";
  std::cout << "Yet, despite the ominous atmosphere, there's a sense of curiosity driving you forward.";
  std::string forward;
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Push forward or return? \n"; std::cin >> forward;  system("cls");
  
  while (forward == "return") {
    srand(time(NULL));  int mozzanswer = std::rand() % 3;
    switch (mozzanswer) {
      
      case 0:
        std::cout << "MOZZ: We have come this far come on we cant turn back now!";
        std::cout << " \n"; std::cout << " \n";
        std::cout << "Push forward or return? \n"; forward = ""; std::cin >> forward;
        system("cls");
        break;
      
      case 1:
        std::cout << "MOZZ: Mamma Dont raise no baby! lets go!";
        std::cout << " \n"; std::cout << " \n";
        std::cout << "Push forward or return? \n"; forward = ""; std::cin >> forward;
        system("cls");
        break;
      
      case 2:
        std::cout << "MOZZ: I did not come this far to turn around now!";
        std::cout << " \n"; std::cout << " \n";
        std::cout << "Push forward or return? \n"; forward = ""; std::cin >> forward;
        system("cls");
        break;
      
      default:
        std::cout << "MOZZ: Man hurry up i need this 10a deal. I will save ya drah if you come!";
        std::cout << " \n"; std::cout << " \n";
        std::cout << "Push forward or return? \n"; forward = ""; std::cin >> forward;
        system("cls");
        break;

    }
  }
  system("cls");
  if (forward == "forward") {

  std::cout << "You and Mozz press on, your footsteps muffled by the thick layer of moss that carpets the forest floor. \n";
  std::cout << "The air grows cooler, and shafts of sunlight pierce through the dense foliage, illuminating patches of vibrant wildflowers.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Suddenly, you hear a faint rustling coming from the north. \n" ;
  std::cout << "Mozz's eyes widen in alarm, and you exchange a nervous glance. \n";
  std::cout << "Whatever lies in that direction, it could hold the key to unlocking the mysteries of this enchanted forest.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "With a shared determination, you and Mozz set off towards the source of the strange noises, \n";
  std::cout << "ready to confront whatever awaits you in the depths of the " << location << " forest.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "As you traverse deeper into the dense foliage, a sense of urgency grips you, urging you forward with each step.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Before long, the forest thins, giving way to a dilapidated entrance obscured by overgrown vines and tangled roots. \n";
  std::cout << "Peering through the dense foliage, you and Mozz catch sight of a shadowy figure slipping stealthily into the city's outskirts. \n";
  std::cout << "Its movements are swift and deliberate, shrouded in mystery and intrigue.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Recognizing the urgency of the situation, you exchange a silent glance with Mozz, \n";
  std::cout << "a shared determination burning in your eyes. Without hesitation, \n";
  std::cout << "you follow the figure into the depths of the city, your senses heightened and adrenaline coursing through your veins. \n";
  std::cout << "Whatever secrets lie within the city's confines, \n";
  std::cout << "you are determined to uncover them and confront the darkness that threatens " << location << ".";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[Press any key Then press Enter, to move to the next page]";
  std::cin >> nextpage;  system("cls");

  }
  return 0;
}

// middle gates
int gates(std::string location, std::string nextpage) {

  std::cout << " \n"; std::cout << " \n";
  std::cout << "INT. DISTANT KINGDOM - DAY";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "You and Mozz arrive at the gates of the fabled " << location << " kingdom. \n";
  std::cout << "The towering walls loom overhead, adorned with intricate carvings that tell the stories of ages past. \n";
  std::cout << "Guards clad in gleaming armor stand watch, their eyes sharp and vigilant.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "MOZZ: (whispering) Do you think they'll let us in?";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "YOU: (shrugging) Only one way to find out.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "With cautious steps, you approach the guards, your heart pounding in anticipation. \n";
  std::cout << "They eye you with suspicion, their hands resting on the hilts of their swords.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "GUARD 1: Halt! State your business.";
  std::string business; //initiates business variable this is just a place holder and has no impact
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Think of a lie to tell the guard! \n"; std::cin >> business; system("cls");
  std::cout << "GUARD 1: I Don't believe you, now scram! AWAY WITH YOU!";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "You exchange a nervous glance with Mozz, unsure of how to proceed. \n";
  std::cout << "This kingdom holds countless secrets, and gaining entry could be the first step towards unraveling its mysteries. \n";
  std::cout << "But with the guards blocking your path, it seems that entering the kingdom won't be easy.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "As you weigh your options, you notice a shadowy figure lurking in the shadow's nearby. \n";
  std::cout << "It beckons to you, its eyes gleaming with an otherworldly light. \n";
  std::cout << "Could this be a sign? A hidden passage, perhaps, that could lead you into the heart of the kingdom undetected?";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "With a silent agreement, you and Mozz turn away from the guards and \n";
  std::cout << "follow the mysterious figure into the darkness, \n";
  std::cout << "ready to uncover the secrets that lie hidden within the walls of the " << location << " kingdom.";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[Press any key Then press Enter, to move to the next page]";
  std::cin >> nextpage;  system("cls");
return 0;
}

int midendtransition(std::string location, std::string nextpage) {

    //walking with figure to the ending
    std::cout << "As you and Mozz follow the mysterious figure through the dimly lit alleys of " << location << ", \n";
    std::cout << "a palpable tension hangs in the air. The figure moves with purpose, \n";
    std::cout << "his steps quick and determined, leading you deeper into the heart of the city.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "MYSTERIOUS FIGURE: (voice echoing in the darkness) The Dark Crack Sorcerer's grip on " << location << " tightens with each passing day. \n";
    std::cout << "His dark magic corrupts everything it touches, twisting the very fabric of reality.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "MOZZ: (whispering) What do you mean? How can one sorcerer have so much power?";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "MYSTERIOUS FIGURE: The Dark Crack Sorcerer's lust for power knows no bounds. \n";
    std::cout << "He seeks to bend the world to his will, to rule over " << location << " with an iron fist. \n";
    std::cout << "But his ambitions come at a terrible cost, for his magic is fueled by darkness and despair.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "YOU: (determined) We can't let him get away with this. " << location << " deserves better.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "As you walk, the figure continues to speak, recounting tales of the sorcerer's atrocities \n";
    std::cout << "and the suffering he has inflicted upon the city. With each word, your resolve strengthens, \n";
    std::cout << "and you know that you must confront the Dark Crack Sorcerer and put an end to his reign of terror once and for all.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "[Press any key Then press Enter, to move to the next page]";
    std::cin >> nextpage;  system("cls");

    //encountering the badguyyy
    std::cout << "[INT. DARK CRACK SORCERER'S LAIR - NIGHT]";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "You and Mozz cautiously navigate through the dark, twisting corridors of the sorcerer's lair, \n";
    std::cout << "the air thick with the stench of dark magic. As you delve deeper, \n";
    std::cout << "you can feel the oppressive weight of the sorcerer's power pressing down on you.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "Suddenly, you come face to face with the Dark Crack Sorcerer himself, a menacing figure cloaked in shadows. \n";
    std::cout << "His eyes gleam with malevolence as he raises his staff, ready to unleash his dark magic upon you. \n";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "DARK CRACK SORCERER: Foolish mortals! You dare to challenge me?";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "With bravery in your hearts, you and Mozz stand firm, ready to face the sorcerer head-on. \n";
    std::cout << "A fierce battle ensues, magic crackling through the air as you clash with the forces of darkness.";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "[Press any key Then press Enter, to move to the next page]";
    std::cin >> nextpage;  system("cls");

return 0;
}

int victory(std::string location) {
    std::cout << "[Victory]";
    std::cout << "Despite the crack sorcerer's formidable power, you and Mozz refuse to back down. \n";
    std::cout << "With a final surge of strength, you deliver a decisive blow that shatters the crack sorcerer's defenses, leaving him vulnerable. \n";
    std::cout << "In a moment of triumph, you seize the opportunity and deliver the finishing blow, \n";
    std::cout << "banishing the crack from " << location << " once and for all. As the sorcerer's power fades, the city erupts in celebration, grateful for your bravery and sacrifice.";

return 0;
}

int loss(std::string location) {

    std::cout << "[LOSS]";
    std::cout << "Despite your valiant efforts, the Dark Crack Sorcerer proves to be too powerful, overwhelming you and Mozz with his crack magic. \n";
    std::cout << "As you lie battered and defeated, the sorcerer looms over you, his laughter echoing in the chamber. \n";
    std::cout << "With a wave of his hand, he seals your fate, condemning " << location << " to a future of crack and despair. \n";
    std::cout << "Your defeat marks the beginning of a new era of tyranny, as the sorcerer's reign of crack goes unchallenged.";

return 0;
}

int sacrifice(std::string location) {

    std::cout << "[SACRIFICE]";
    std::cout << "Realizing that defeating the Dark Crack Sorcerer may require a sacrifice, \n";
    std::cout << "you and Mozz make the ultimate decision to channel all your remaining strength and magic into a final, desperate attack. \n";
    std::cout << "With a blinding flash of light, you unleash a devastating blast that engulfs both you and the sorcerer in crack. \n";
    std::cout << "As the dust settles, " << location << " is left in ruins, but the crack has been vanquished. \n";
    std::cout << "Your sacrifice is not in vain, whilst you mozz and the sorcerer are hooked for life, \n";
    std::cout << "the city is free from crack once again, and your memory lives on as heroes who gave everything to save those they loved. \n";

return 0;
}

int main() {

  std::string nextpage;


  //beginning of the story
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[You find yourself in a cozy room, dimly lit with a warm glow. \n";
  std::cout << "Two friends, you and Mozz, eagerly await the arrival of your esteemed \n";
  std::cout << "professor, Prof. Wang. The air buzzes with excitement as you exchange glances, \n";
  std::cout << "wondering where your adventure will take you.] \n";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "YOU: (to Mozz) Hey Mozz, where do you think our story should begin? \n";
  std::cout << " \n"; std::cout << " \n";
  

  //First User input for a Town decided to give mozz abit of personality and have him reject first option.
  std::cout << "Enter a Town. \n";
  std::string location; std::cin >> location; system("cls"); //decalre location variable
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[Mozz considers the options for a moment, then Sighs in disagreement.] \n";
  std::cout << " \n"; std::cout << " \n";

  // New Town Location
  
  std::cout << "Enter a New Town. \n";
  location = ""; std::cin >> location; system("cls"); //cls the variable 
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[Mozz considers the options for a moment, then nods in agreement.] \n";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[You both exchange a shudder at the thought.] \n";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "YOU: " << location << " it is then! \n";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "[The scene fades out as you prepare to embark on your adventure in the dreaded land of " << location << " ...] \n";
  std::cout << " \n"; std::cout << " \n";
  std::cout << "Where should we pick the story up? \n  1) The forests of " << location << "? \n  2) The gates of " << location << " \n";

  int middle_choice; std::cin >> middle_choice; system("cls");

  while (middle_choice != 1 && middle_choice != 2) {

    std::cout << "Invalid choice please pick either 1 or 2 to progress to the next section";
    std::cout << " \n"; std::cout << " \n";
    std::cout << "Where should we pick the story up? \n  1) The forests of " << location << "? \n  2) The gates of " << location << " \n";
    std::cin >> middle_choice; system("cls");   

  }; if (middle_choice == 1) {

    forest(location, nextpage); // middle path of story but at forest

  } else if (middle_choice == 2) {

    gates(location, nextpage); // middle path of story but at gate
    
  }
   
   midendtransition(location, nextpage); // mid end innit
   std::cout << "Type 'Finish this' Then press enter to Roll the Dice and decide the outcome! Hurry you dont have long! \n";
   std::string rolldice; std::cin >> rolldice;  system("cls");

    srand(time(NULL));  int roll = std::rand() % 3;

    switch (roll) {

        case 0:
          victory(location);
          break;
        
        case 1:
          sacrifice(location);
          break;

        case 2:
          loss(location);
          break;

    }

   }
   




