# 🐍 HTX API Authenticator

> USe Ed25519 better!!!
> A Python desktop tool for secure API communication using **Ed25519** signatures, **HMAC authentication**, and a **Tkinter GUI** interface.

<!-- <p align="center">
  <img src="assets/demo.png" width="420" alt="App Demo">
</p> -->

---

## ⚙️ Features

✅ Send and receive data securely through the HTX API  
✅ Generate and verify **Ed25519** signatures  
✅ Generate and verify **HMAC** signatures  
✅ Simple and intuitive **Tkinter** GUI  
✅ Clean, modular Python architecture

---

## 🧠 Tech Stack

| Component          | Description                      |
| ------------------ | -------------------------------- |
| 🐍 Python 3.12     | Core programming language        |
| 🪪 Ed25519          | Public-key signature system      |
| 🔒 HMAC            | Message authentication           |
| 🧰 HTX API         | RESTful API endpoint integration |
| 🖥️ Tkinter         | GUI for user interactions        |
| 🖥️ cryptography    | creating signature and signing   |
| 🖥️ aiohttp/asyncio | get/post data from/to api        |

- other needed packages

---

## 🚀 Installation

1. **Clone the repository**

```bash
git clone https://github.com/videikisairidas/htx-api-python.git
```

2. **create venv ( before install python)**

```
python3 -m venv .venv
```

2.1 **vsc select enviroment python**

```
ctrl + shift + p
```

2.2 **activate venv**

```
.\.venv\Scripts\activate
```

**3. install packages**

```
pip install -r htx_api_python/z_requirements.txt
python -m pip install --upgrade pip
```

**4. setup .env**

```
copy/rename .env.example -> .env
```

**5.a if you want use ed25519,**

```
create public and private keys
Run htx-api-python/HTX_Manage/\_createEd25519/create.py
Create a key and public it: copy text from ed25519-public.pem **without 1 and 3 lines** to ed25519 **[htx](https://www.htx.com/apikey/)**
Copy created key **access_key** and put to .env -> HTX_Ed25519_ACCESS_KEY
```

**5.b using HMACSHA256**

```
Create access_key and secret_key in **[htx](https://www.htx.com/apikey/)**
Copy both to .env HTX_ACCESS_KEY and HTX_SECRET_KEY
```

**6.a run tk UI/main.py**

```
run htx-api-python/main.py with tk UI
```

**6.b run terminal examples**

```
run htx-api-python/example/ed25519/get_account.py
or
run htx-api-python/example/hmac/get_account.py
```

## 🧾 Version History & Updates

| Version | Changes                                                                 |
| ------- | ----------------------------------------------------------------------- |
| v0.0.1  | 🧱 Initial release with Ed25519 + HMAC + Tkinter GUI. (for testing api) |

## 📜 License

Licensed under the MIT License © 2025 videikisairidas

# 💬 Support

Need help or want to share feedback?-
You can reach out here:

📧 Discord: [Discord](https://discord.gg/PSDD6HJhpx)

Telegram Private msg: [Text me](https://t.me/airis_whatever)

# 💖 Support My Work

If you find this project helpful, consider supporting me:

[![Donate](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-yellow.svg)](https://buymeacoffee.com/maxyou200)
