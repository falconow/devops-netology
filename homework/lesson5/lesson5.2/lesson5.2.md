> С системами виртуализации в практике не сталкивался, постараюсь ответить на вопросы полностью 
> опираясь на лекцию

### Задание 1
1. VMWare
 >Т.к. используем одновременно и Linux и Windows, и не затрагивается финансовая сторона вопроса я бы 
> предпочел использовать систему с хорошей поддержкой и безопасностью.

2. KVM
> Здесь также используем системы Windows и Linux. В условии задана максимальная производительность и 
> бесплатное решение, поэтому остановим выбор на KVM.

3. KVM
> Т.к. у нас  Windows инфраструктура и решение бесплатное, KVM лучше адаптирован с работой Windows

4. VirtualBox
> Я бы использовал это решение т.к. оно бесплатное, и позволяет быстро поднять несколько виртуальных
> машин в рабочей ОС

### Задание 2
> Изучив вопрос в интернете пришел к выводу что каждый гипервизор работает со своим форматом жесткого
> диска. Поэтому весь процесс миграции сводится к конвертации формата жесткого диска первого гипервизора 
> в формат второго гипервизора. Создается новая виртуальная машина и к ней подключают переконвертированный диск.
> В интернете приводятся разные утилиты для конвертации жестких дисков виртуальных машин(VirtualBox, 
> Microsoft Virtual Machine Migration Toolkit, V2V Converter и т.д.)


### Задание 3
> Достаточно сложно ответить на этот вопрос, т.к. не опыта работы с такими системами. Думаю что 
> использовать несколько гипервизоров это плохая идея. Каждый гипервизор управляет ресурсами железа.
> Думаю может возникнуть что-то типа конфликта, когда каждый гипревизор начнет использовать одни и те же
> ресурсы железа. Что-то похожее на конфликт ip адресов в сети(первое что пришло на ум для сравнения).
> Такая ситуация может привести к снижению производительности или может привести к неработоспособности
> виртуальной машины в целом.
> Я бы использовал вариант с одной системой управления виртуализацей. Чем проще система, программа и т.д. 
> тем стабильнее работает система. Ни к чему лишний раз производить усложнения.




