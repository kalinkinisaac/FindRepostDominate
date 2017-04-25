# Contributing guide

### Подготовка
Вся информация об SSH в github
https://help.github.com/articles/connecting-to-github-with-ssh/

Настройка SSH своего github аккаунта
https://help.github.com/articles/checking-for-existing-ssh-keys/
https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#adding-your-ssh-key-to-the-ssh-agent
https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/

После настройки SSH скачиваем проект в свой репозиторий
git clone git@github.com:kalinkinisaac/Pharaoh.git

### Создание окружения
Откройте PyCharm, в нем создайте новый проект в папке Pharaoh (версия питона - 3.*)
Когда среда предложит установить доп. пакеты из requirements.txt, установите их
### Разрабатываемые классы
Названия, поля и описание классов можно посмотреть на [этой диаграмме](https://gliffy.com/go/publish/11961848)

Имена методов и аргументов vk api wrapper'а полностью совпадают с теми, что представлены в [официальной документации](https://vk.com/dev/manuals)
### Config
Для запуска проекта требуется файл `source/cofig/config.cfg`, где находятся логин и пароль бота
