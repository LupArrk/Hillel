SchoolersNmbr = int(input('Сколько школьников хотят яблоки?'"\n"))
ApplesInBusket = int(input('Сколько сколько яблок лежит в корзине?'"\n"))

print('Каждый школьник получит следующее количество яблок:',int(ApplesInBusket / SchoolersNmbr),'шт.'
       '\n''В корзине останется:', int(ApplesInBusket % SchoolersNmbr),'шт.')

print('\n''**************************************************************************')

DeskCapacity = 2
SchoolersNmbrFrstClass = int(input('Сколько школьников поступят в первый класс?'"\n"))
SchoolersNmbrScndClass = int(input('Сколько школьников поступят во второй класс?'"\n"))
SchoolersNmbrThirdClass = int(input('Сколько школьников поступят в третий класс?'"\n"))

TotalNerdsNmbr = (SchoolersNmbrFrstClass + SchoolersNmbrScndClass + SchoolersNmbrThirdClass)
RawInfo = (TotalNerdsNmbr / DeskCapacity)
ResultNumber = int((TotalNerdsNmbr % DeskCapacity) + RawInfo)

print('Всего необходимо парт:',ResultNumber,'шт.')

print('\n''**************************************************************************')



n1 = int(input('Введите число:'))

n2 = 0
while n1>0:
    digit = n1%10
    n1= n1 // 10
    n2 = n2*10 + digit
print (n2)

print('\n''**************************************************************************')

InputTime= int(input('Введите количество секунд:'"\n"))

MinutesCount = int(InputTime / 60)
SecondsCount = int(InputTime % 60)

if MinutesCount > 60:
    HoursCount = (MinutesCount // 60)
    MinutesCount  = MinutesCount % 60
else:
    HoursCount = 0
    MinutesCount = int(InputTime / 60)
    SecondsCount = int(InputTime % 60);

if InputTime < 60:
    print(00, ':', 00, ':', InputTime)
else:
    print (HoursCount,':',MinutesCount,':',SecondsCount);
