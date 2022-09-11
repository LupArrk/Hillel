SchoolersNmbr = int(input('Сколько школьников хотят яблоки?'"\n"))
ApplesInBusket = int(input('Сколько сколько яблок лежит в корзине?'"\n"))

print('Каждый школьник получит следующее количество яблок:',int(ApplesInBusket / SchoolersNmbr),'шт.'
       '\n''В корзине останется:', int(ApplesInBusket % SchoolersNmbr),'шт.')

print('\n''**************************************************************************')

MathClaseesNubmer = 3
DeskCapacity = 2
SchoolersNmbrFrstClass = int(input('Сколько школьников поступят в первый класс?'"\n"))
SchoolersNmbrScndClass = int(input('Сколько школьников поступят во второй класс?'"\n"))
SchoolersNmbrThirdClass = int(input('Сколько школьников поступят в третий класс?'"\n"))

RawInfo = ((SchoolersNmbrFrstClass + SchoolersNmbrScndClass + SchoolersNmbrThirdClass) / DeskCapacity)
ResultNumber = int(((SchoolersNmbrFrstClass + SchoolersNmbrScndClass + SchoolersNmbrThirdClass) / DeskCapacity)
                   + (RawInfo % DeskCapacity/DeskCapacity))

print('Всего необходимо парт:',ResultNumber,'шт.')

print('\n''**************************************************************************')
