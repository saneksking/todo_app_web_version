# ToDo App Web <sup>v0.0.1</sup>

---
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/saneksking/todo_app_web_version)](https://github.com/saneksking/todo_app_web_version/)
![GitHub top language](https://img.shields.io/github/languages/top/saneksking/todo_app_web_version)
[![GitHub](https://img.shields.io/github/license/saneksking/todo_app_web_version)](https://github.com/saneksking/todo_app_web_version/blob/master/LICENSE)
---

**TODO App web** - simple, comfortable and affordable web-application for kepting and compleating your tasks.

---

## Help:

### MariaDb:

- `sudo systemctl stop mysqld`
- `sudo pacman -S mariadb libmariadbclient mariadb-clients`
- `sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql`
- `sudo systemctl start mariadb`
- `sudo mysql_secure_installation`
- `sudo systemctl restart mariadb`
- `sudo mysql -u root -p`

- `CREATE USER 'USER_NAME'@'localhost' IDENTIFIED BY 'PASSWORD';`
- `CREATE DATABASE database_name CHARACTER SET utf8 COLLATE utf8_general_ci;`
- `GRANT ALL PRIVILEGES ON database_name.* TO 'USER_NAME'@'localhost';`
- `FLUSH PRIVILEGES;`
- `exit`


- Clone project
- Go to your project folder

---

### Requirements:

- `python -m venv venv`
- `source venv/bin/activate`
- `pip install --upgrade pip`
- `pip install -r requirements.txt`

---

### Create file .env in your project:

```env
SECRET_KEY="<your django secret key>"
DB_NAME="todo_app_web_db"
DB_USER="todo_app_web_user"
DB_PASSWORD="<password>"
DB_HOST="localhost"
```

---

## Run:

- `python manage migrate`
- `python manage createsuperuser`
- `python manage.py runserver`
- You can open in browser [here](http://127.0.0.1:8000)

---

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

---

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
