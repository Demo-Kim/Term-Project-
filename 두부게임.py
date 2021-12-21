import random
com_num={ 1: '두부 한 모', 2: '두부 두 모' , 3: '두부 세 모', 4: '두부 네 모', 5:'두부 다섯 모'}
com_str={'두부 한 모':1, '두부 두 모':2 , '두부 세 모':3, '두부 네 모':4, '두부 다섯 모':5}

print('''<두부게임 설명>
          1. 각 플레이어는 1~5번으로, 그 중 사용자는 5번 플레이어 입니다.
          2. 플레이어는 '두부 ?모'를 외칩니다.
          3. 두부는 '한 모'부터 '다섯 모'까지 있으며 플레이어 번호와 동일합니다. 
              ex) 1번 - 한 모, 5번(사용자) - 다섯 모 
          4. 자기 자신을 외칠 수 없습니다.
          ''')
turn = random.randint(1, 5)

while True:

        
    start = input("> 게임을 시작하시려면 '시작'을 입력하세요.")
        
    if start == '시작' :
        you = input("> 당신의 차례입니다. ")
        if you == '두부 다섯 모' :
            print('YOU : 두부 다섯 모\n\n'
                     '>>> 당신이 졌습니다.')
            break
        else :
            print('YOU : : ',you) 
            turn = com_str[you]
            print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
        
        while True:
            rand = random.randint(1, 5)
                
            if rand==1:
                com = '두부 한 모'
            elif rand==2:
                com = '두부 두 모'
            elif rand==3:
                com = '두부 세 모'
            elif rand==4:
                com = '두부 네 모'
            elif rand==5:
                com = '두부 다섯 모'
            
                  
            
           #사용자         
            if turn == 5 :
                you = input("> 당신의 차례입니다.")
                if you == com_num[turn] :
                    print('YOU : ',com,'\n\n'
                     '>>> 당신이 졌습니다.') 
                    break         
                elif you == '두부 한 모' :
                    print(turn,'번 플레이어 : ',you) 
                    turn = com_str[you]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                elif you == '두부 두 모' :
                    print(turn,'번 플레이어 : ',you) 
                    turn = com_str[you]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                elif you == '두부 세 모' :
                    print(turn,'번 플레이어 : ',you) 
                    turn = com_str[you]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                elif you == '두부 네 모' :
                    print(turn,'번 플레이어 : ',you) 
                    turn = com_str[you]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                else :
                    print('> 올바른 입력이 아닙니다. 처음부터 다시 시작합니다.')
                    break
                
            #컴퓨터
            elif turn==1 or you == '두부 한 모':                 
                if com == com_num[turn] :
                    print(turn,'번 플레이어 : ',com,'\n\n'
                      '>>> ',turn,'번 플레이어가 졌습니다.')
                    break
                else :
                    print(turn,'번 플레이어 : ',com)
                    turn = com_str[com]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                    
            elif turn==2 or you == '두부 두 모':
                if com == com_num[turn] :
                    print(turn,'번 플레이어 : ',com,'\n\n'
                      '>>> ',turn,'번 플레이어가 졌습니다.')
                    break
                else :
                    print(turn,'번 플레이어 : ',com)
                    turn = com_str[com]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
                    
            elif turn==3 or you == '두부 세 모':
                if com == com_num[turn] :
                    print(turn,'번 플레이어 : ',com,'\n\n'
                      '>>> ',turn,'번 플레이어가 졌습니다.')
                    break
                else :
                    print(turn,'번 플레이어 : ',com) 
                    turn = com_str[com]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
            elif turn==4 or you == '두부 네 모':
                if com == com_num[turn] :
                    print(turn,'번 플레이어 : ',com,'\n\n'
                      '>>> ',turn,'번 플레이어가 졌습니다.')
                    break
                else :
                    print(turn,'번 플레이어 : ',com) 
                    turn = com_str[com]
                    print('> 다음 차례는 ', turn,'번 플레이어 입니다.\n')
         
    else:
        print("> 잘못 입력했습니다. '시작'을 정확하게 입력해주세요.")    
        continue        
    
