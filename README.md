# django_template
A basic template for you to get started using Django in your projects.
Follow guides here: 

- [How to set up VS code Studio](https://youtu.be/v5eRARe5PVE)
- [How to download github repo to VS Code Studio](https://youtu.be/30OY8aeaFaQ)
- [What are branches and merging + how to create them](https://www.youtube.com/watch?v=S7TbHDN8EXA)

## Virtual Environment settings

### installing env settings from the django template
open terminal in the root of the project folder and:

```bash
    pip install -r requirements.txt
```

### saving env settings
In order to save settings from your virtual environment when uploading onto GitHub, there must be a file called `requirements.txt` in the root of your project.

To save the settings and currently installed add ons open terminal in your project directory and type:

```bash
    pip freeze > requirements.txt
```