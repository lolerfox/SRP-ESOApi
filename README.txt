Для читабельности текста данное окошко можно растянуть.
_________________________
Версия данного текста с картинками: shorturl.at/opzCN
_________________________

SRP ESO - Простенький скрипт написанный с целью упростить и разнообразить RP процесс.

Он предоставляет базовые “шорткаты” и возможность быстрой, комфортной отыгровки ситуаций через систему Кубиков и Успехов.

Почему кубики? Все просто... /try очень ограничен в своих ситуативных возможностях...

К примеру: Хрупкая по своей натуре девушка пытается отбиться от обижающих ее пионеров... и о чудо с шансом в 50`% процентов ей удается это сделать... По моему мнению это странно.

Система Умений и Кубиков позволяет более лаконично найти выход из этой ситуации.

К примеру: Если у выше упомянутой девушки параметр Силы будет равен 2, а у обижающих ее пионеров он будет гораздо выше… То понятное дело что применять силу будет не целесообразно, а значит что в ход нужно пустить Ловкость(дабы избежать напорства пионеров), либо Харизму что бы попытаться найти выход не силой, а словами.

Возможно для тех кто ранее играл в настольные ролевы игры данная система будет знаком и не нуждается в пояснении.
Но для не знакомых с данной системой людей объясняю :)
_________________________

Как же это работает система Кубиков и Успехов?

Для начала про Успех:

Здесь все кратко и понятно…
Успехом принято считать если на Кубике выпадет 5 или 6.
У кого больше Успехов тот и победил.
_________________________

Теперь про процесс отыгровки.

Возьмем для примера такие характеристики:
-Для Персонажа1: Сил 7 Лов 6 Инт 4 Хар 4 Удч 4
-Для Персонажа2: Сил 1 Лов 8 Инт 8 Хар 3 Удч 5

П1 решает схватить П2 за руку используя Силу.
“П1: *схватил П2 за руку*”

“П1: */dice 7d6*”(Характеристика силы П1 равна 7, значит ему нужно кинуть 7 кубиков.)
Ему выпадают такие значения “rolled 5/6 3/6 5/6 1/6 6/6 4/6 2/6”(выпало 3 успеха)

П2 анализируя ситуацию понимает что ему бесполезно использовать силу так как она равна 1 и даже если ему и выпадет Успех, то этого явно будет маловато(1<3).

П2 должен показать то что он проиграл в данном коне.
“П2: *пытается вырвать руку*”

После П2 применяет Ловкость для того что бы попытаться выбраться.
“П2:/dice 8d6”
Ему выпадают такие значения “rolled 6/6 6/6 5/6 1/6 1/6 2/6 4/6 5/6”(Выпало 4 успеха.)

Исход данного кона: П2 Вырвал свою руку из захвата П1 (4>3).

Небольшая сноска… По правилам настольных RPG нельзя до бесконечности продолжать коны. Всегда есть разумное ограничение… Как правило, если второй игрок смог победить в коне, то первый игрок не должен пытаться помешать ему, повторяя действие.
Ну и не стоит использовать нелогичные ходы... Против силы выдвигать удачу.
_________________________

А теперь немного об интерфейсе скрипта и его настройке.

AOTandSO:
Простой скрипт на AHK для того что бы быстро взаимодействовать с скриптом.
F1: Открыть окно SRP ESO
F2: Седлать окно SRP ESO всегда поверх других окон.
F3: Отключить режим “Поверх других окон”
_________________________

Для начала в чат нужно отправить команду “/notf” после чего должно появиться
уведомление “Notifier enabled”, после можно запускать сам скрипт.

Вкладка Main:
Данная вкладка работает на “шорткатах”(подписаны рядом с кнопкой) либо по нажатию на элемент интерфейса.

Вкладка Config:
Данная вкладка предназначена для создана и редактирования
конфигов.
Начнем с добавления профилей конфигов для персонажей.

1)Вести имя конфига в нижнее поле над кнопкой добавить.
Советую не перегружать имя конфига, и не использовать сторонние символы, в особенности различные скобки.

2)После создания конфиг будет автоматически выбран.
(Для удаления выбрать конфиг в  “комбо-боксе” и нажать “Delete”)

3)Заполняете поля нужными данными.

С полями имени и информации я думаю все очевидно.

Немного про навыки.
Я использую сильно упрощенную систему из 5 навыков и 25 очков.
Strength - Сила.                   Сharisma - Харизма.
Agility - Ловкость.                Luck - Удача.
Intellegence - Интеллект.

Этого вполне достаточно и выглядит сбалансировано.

Если вы используете более 25 очков программа будет оповещать в чат о том что вы играете не совсем честно

Так же если есть свободные очки программа тоже оповестит об этом.

Я не планирую делать обфускацию кода или компиляцию в исполняемый файл… если вы правите код так что бы снять данные ограничения… все будет на вашей совести!

4)Нажимаете “Save”

5)Готово! Теперь в Main будут обновлены данные конфига.

_________________________

На этом я думаю все…
Спасибо, что используете скрипт и…
Приятной отыгровки вам!<3
