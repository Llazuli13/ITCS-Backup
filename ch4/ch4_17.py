import random
while True:
  print('Pumpkin crushes spider, spider poisons vampire, vampire carves pumpkin.')
  playerChoice = eval(input('Pumpkin (0), Spider (1) or Vampire(2)? '))
  if playerChoice == 0:
    print('                           .,`')
    print('                       .``.`')
    print('                      .` .`')
    print('          _.ood0Pp._ ,`  `.~ .q?00doo._')
    print('      .od00Pd0000Pdb._. . _:db?000b?000bo.')
    print('    .?000Pd0000Pd0000PdbMb?0000b?000b?0000b.')
    print('  .d0000Pd0000Pd0000Pd0000b?0000b?000b?0000b.')
    print('  d0000Pd0000Pd00000Pd0000b?00000b?0000b?000b.')
    print('  00000Pd0000Pd0000Pd00000b?00000b?0000b?0000b')
    print('  ?0000b?0000b?0000b?00000Pd00000Pd0000Pd0000P')
    print('  ?0000b?0000b?0000b?00000Pd00000Pd0000Pd000P')
    print('  `?0000b?0000b?0000b?0000Pd0000Pd0000Pd000P`')
    print('    `?000b?0000b?000b?0000Pd000Pd0000Pd000P')
    print('      `~?00b?000b?000b?000Pd00Pd000Pd00P`')
    print('          `~?0b?0b?000b?0Pd0Pd000PdP~`')
  elif playerChoice == 1:
    print('   /\  .-===-.  /\ ')
    print('  //\\/  ,,,  \//\\')
    print('  |/\| ,;;;;;, |/\|')
    print('  //\\\;-"""-;///\\')
    print(' //  \/   .   \/  \\')
    print('(| ,-_| \ | / |_-, |)')
    print('  //`__\.-.-./__`\\')
    print(' // /.-(() ())-.\ \\')
    print('(\ |)   `---`   (| /)')
    print(' ` (|           |) `')
    print('   \)           (/')
  else:
    print('                 /######\ ')
    print('               /##########\ ')
    print('              /   \###/    \ ')
    print('             /     \#/      \ ')
    print('          /\|               |/\ ')
    print('          | | \ ==\    /== / | |')
    print('           \|  \<|>\  /<|>/  |/     /|')
    print('    \__     |    -   \  -    |     /#|')
    print('     \#\     |        |      |   /###|')
    print('      \##\   |       \|     |  /#####|')
    print('       \###\  |   _______  | /######|')
    print('        \####\ | / \/ \/ \|/#######|')
    print('        |######\|        |#########|')
    print('        |########\______/##########|')
    print('        |#########\    /##########/')
    print('        |##########\  |#########/\ ')
    print('        /###########\/########/###\ ')
    print('    /################\######/########\ ')
    print('   /##################\###/###########\ ')
    print('  /###################\#/##############\ ')
    print(' /####################/#################\ ')
    print('/###################/####################\ ')
  print('\t')
  computerChoice = random.randint(0, 2)
  print('Opponent:')
  if computerChoice == 0:
    print('                           .,`')
    print('                       .``.`')
    print('                      .` .`')
    print('          _.ood0Pp._ ,`  `.~ .q?00doo._')
    print('      .od00Pd0000Pdb._. . _:db?000b?000bo.')
    print('    .?000Pd0000Pd0000PdbMb?0000b?000b?0000b.')
    print('  .d0000Pd0000Pd0000Pd0000b?0000b?000b?0000b.')
    print('  d0000Pd0000Pd00000Pd0000b?00000b?0000b?000b.')
    print('  00000Pd0000Pd0000Pd00000b?00000b?0000b?0000b')
    print('  ?0000b?0000b?0000b?00000Pd00000Pd0000Pd0000P')
    print('  ?0000b?0000b?0000b?00000Pd00000Pd0000Pd000P')
    print('  `?0000b?0000b?0000b?0000Pd0000Pd0000Pd000P`')
    print('    `?000b?0000b?000b?0000Pd000Pd0000Pd000P')
    print('      `~?00b?000b?000b?000Pd00Pd000Pd00P`')
    print('          `~?0b?0b?000b?0Pd0Pd000PdP~`')
  elif computerChoice == 1:
    print('   /\  .-===-.  /\ ')
    print('  //\\/  ,,,  \//\\')
    print('  |/\| ,;;;;;, |/\|')
    print('  //\\\;-"""-;///\\')
    print(' //  \/   .   \/  \\')
    print('(| ,-_| \ | / |_-, |)')
    print('  //`__\.-.-./__`\\')
    print(' // /.-(() ())-.\ \\')
    print('(\ |)   `---`   (| /)')
    print(' ` (|           |) `')
    print('   \)           (/')
  else:
    print('                 /######\ ')
    print('               /##########\ ')
    print('              /   \###/    \ ')
    print('             /     \#/      \ ')
    print('          /\|               |/\ ')
    print('          | | \ ==\    /== / | |')
    print('           \|  \<|>\  /<|>/  |/     /|')
    print('    \__     |    -   \  -    |     /#|')
    print('     \#\     |        |      |   /###|')
    print('      \##\   |       \|     |  /#####|')
    print('       \###\  |   _______  | /######|')
    print('        \####\ | / \/ \/ \|/#######|')
    print('        |######\|        |#########|')
    print('        |########\______/##########|')
    print('        |#########\    /##########/')
    print('        |##########\  |#########/\ ')
    print('        /###########\/########/###\ ')
    print('    /################\######/########\ ')
    print('   /##################\###/###########\ ')
    print('  /###################\#/##############\ ')
    print(' /####################/#################\ ')
    print('/###################/####################\ ')
  print('\t')
  if playerChoice == 0 and computerChoice == 0:
    print('It\'s a tie!')
  elif playerChoice == 1 and computerChoice == 1:
    print('It\'s a tie!')
  elif playerChoice == 2 and computerChoice == 2:
    print('It\'s a tie!')
  elif playerChoice == 0 and computerChoice == 1:
    print('You won!')
  elif playerChoice == 1 and computerChoice == 2:
    print('You won!')
  elif playerChoice == 2 and computerChoice == 0:
    print('You won!')
  elif computerChoice == 0 and playerChoice == 1:
    print('You lose.')
  elif computerChoice == 1 and playerChoice == 2:
    print('You lose.')
  elif computerChoice == 2 and playerChoice == 0:
    print('You lose.')
  repeat = input('Would you like to try again? (y/n): ')
  if repeat == 'n':
      break