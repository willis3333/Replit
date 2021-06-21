input('''
                                  ,'\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|
--Welcome to the Pokemon Mystery Adventure! We need your help to find Pikachu. \n\n
--Choose wisely, and make sure your responses are in lowercase and spelled exactly as the options suggest. \n\nGood Luck! (Press ENTER to begin)\n''')
stage1=input('--You are trapped in the lab and must get out.\n\
--You wake up in the storage closet and it is dark. You see two options to get out. A vent or a door handle.\n\
--Which do you chose to "door" or "vent"?\n\n')
if stage1=='vent':
  print('--You fell into a long dark tunnel with no way out. GAME OVER')
elif stage1=='door':
  print('\n--You have exited the storage closet and are now in the main laboratory. \n\n')
  stage2=input('--There is a man in a lab coat working on an experiment. "talk" or "run"?\n\n')
  if stage2=='run':
    print('--The man in the coat was the professor. He did not recognize you and has called security.\n\n\
    --you were caught and escorted to the police. GAME OVER')
  elif stage2=='talk':
    print('\n\n--you ask the man in the labcoat if he has seen pikachu. \n\n\
    --He is the professor.\n\n --He tells you he tells you a group of strange men have broken into the lab and kidnapped many of the Pokemon\n\n\
    --Some are trapped in the closets and others were taken. \n\n\
    --The men mixed up many of his beakers and have not he must fix them so they will not explode.\n\n')
    stage3=input('--You agree to help the professor Look for the Pokemon. There are several doors to check:\n\ntype "blue" for the blue door, \ntype "red" for the red door, or: \ntype "exit" to go outside and look for the men\n\n')
    if stage3=='blue':
      print('''                           /
                        _,.------....___,.' ',.-.
                     ,-'          _,.--"        |
                   ,'         _.-'              .
                  /   ,     ,'                   `
                 .   /     /                     ``.
                 |  |     .                       \.\
       ____      |___._.  |       __               \ `.
     .'    `---""       ``"-.--"'`  \               .  \
    .  ,            __               `              |   .
    `,'         ,-"'  .               \             |    L
   ,'          '    _.'                -._          /    |
  ,`-.    ,".   `--'                      >.      ,'     |
 . .'\'   `-'       __    ,  ,-.         /  `.__.-      ,'
 ||:, .           ,'  ;  /  / \ `        `.    .      .'/
 j|:D  \          `--'  ' ,'_  . .         `.__, \   , /
/ L:_  |                 .  "' :_;                `.'.'
.    ""'                  """""'                    V
 `.                                 .    `.   _,..  `
   `,_   .    .                _,-'/    .. `,'   __  `
    ) \`._        ___....----"'  ,'   .'  \ |   '  \  .
   /   `. "`-.--"'         _,' ,'     `---' |    `./  |
  .   _  `""'--.._____..--"   ,             '         |
  | ." `. `-.                /-.           /          ,
  | `._.'    `,_            ;  /         ,'          .
 .'          /| `-.        . ,'         ,           ,
 '-.__ __ _,','    '`-..___;-...__   ,.'\ ____.___.'
 `"^--'..'   '-`-^-'"--    `-^-'`.''"""""`.,^.`.--' --you open the blue door and find bulbasaur!\n\n\
      you free him and keep looking for Pikachu''')
      stage4 = input('\n\n--There are two doors left to check:\n\ntype  "red" for the red door\n type "exit" to go outside and look for the men:')
      if stage4=='red':
        print('''    \:.             .:/
        \``._________.''/ 
         \             / 
 .--.--, / .':.   .':. \
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
l42        :-._____.-:
          `''       `''--you open the red door and find Pikachu! \n\n--CONGRATULATIONS! You WIN!!''')
      elif stage4== 'exit':
        print('\n\n--The men were waiting outside and attacked you. GAME OVER')
    elif stage3=='red':
      print('''    \:.             .:/
        \``._________.''/ 
         \             / 
 .--.--, / .':.   .':. \
/__:  /  | '::' . '::' |
   / /   |`.   ._.   .'|
  / /    |.'         '.|
 /___-_-,|.\  \   /  /.|
      // |''\.;   ;,/ '|
      `==|:=         =:|
         `.          .'
          :-._____.-:
          `''       `''--you open the red door and find Pikachu! CONGRATULATIONS! You WIN!!''')
    elif stage3== 'exit':
      print('\n\n--The men were waiting outside and attacked you. GAME OVER')