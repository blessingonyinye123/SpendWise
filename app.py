
Conversation with Gemini
WHERE IS LOGS TAB

1
Look at the left-hand sidebar menu
Look at the dark sidebar on the far left side of your screen where it says SpendWise at the top.
Verification: You see options like Environment, Deploys, Settings, etc. listed vertically down that left panel.

2
Click on Logs
Scroll down slightly on that left menu if needed, and click on Logs (it is located right below Metrics or Deploys in that sidebar list).
Verification: The main page view switches to show the live server output and error tracebacks.

==> Deploying...

==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance

==> Running 'gunicorn app:app'

[2026-11-10 13:20:53 +0000] [58] [INFO] Starting gunicorn 27.0.0

[2026-11-10 13:20:53 +0000] [58] [INFO] Listening at: http://0.0.0.0:10000 (58)

[2026-11-10 13:20:53 +0000] [58] [INFO] Using worker: sync

[2026-11-10 13:20:53 +0000] [59] [INFO] Booting worker with pid: 59

[2026-11-10 13:20:54,344] ERROR in app: Exception on / [HEAD]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:20:54 +0000] "HEAD / HTTP/1.1" 500 0 "-" "Go-http-client/1.1"

[2026-11-10 13:20:54 +0000] [58] [INFO] Control socket listening at /opt/render/.gunicorn/gunicorn.ctl

==> Your service is live 🎉

[2026-11-10 13:21:00,502] ERROR in app: Exception on / [GET]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:21:00 +0000] "GET / HTTP/1.1" 500 265 "-" "Go-http-client/2.0"

==> 

==> ///////////////////////////////////////////////////////////

==> 

==> Available at your primary URL https://spendwise-t4qq.onrender.com

==> 

==> ///////////////////////////////////////////////////////////

==> Deploying...

==> Setting WEB_CONCURRENCY=1 by default, based on available CPUs in the instance

==> Running 'gunicorn app:app'

[2026-11-10 13:22:05 +0000] [59] [INFO] Starting gunicorn 27.0.0

[2026-11-10 13:22:05 +0000] [59] [INFO] Listening at: http://0.0.0.0:10000 (59)

[2026-11-10 13:22:05 +0000] [59] [INFO] Using worker: sync

[2026-11-10 13:22:05 +0000] [60] [INFO] Booting worker with pid: 60

[2026-11-10 13:22:05,632] ERROR in app: Exception on / [HEAD]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:22:05 +0000] "HEAD / HTTP/1.1" 500 0 "-" "Go-http-client/1.1"

[2026-11-10 13:22:06 +0000] [59] [INFO] Control socket listening at /opt/render/.gunicorn/gunicorn.ctl

[2026-11-10 13:22:12 +0000] [58] [INFO] Handling signal: term

[2026-11-10 13:22:12 +0000] [59] [INFO] Worker exiting (pid: 59)

[2026-11-10 13:22:13,074] ERROR in app: Exception on / [GET]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:22:13 +0000] "GET / HTTP/1.1" 500 265 "-" "Go-http-client/2.0"

==> Your service is live 🎉

[2026-11-10 13:22:13 +0000] [58] [INFO] Shutting down: Master

==> 

==> ///////////////////////////////////////////////////////////

==> 

==> Available at your primary URL https://spendwise-t4qq.onrender.com

==> 

==> ///////////////////////////////////////////////////////////

[2026-11-10 13:25:04,382] ERROR in app: Exception on / [GET]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:25:04 +0000] "GET / HTTP/1.1" 500 265 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0"

127.0.0.1 - - [10/Nov/2026:13:25:04 +0000] "GET /favicon.ico HTTP/1.1" 404 207 "https://spendwise-t4qq.onrender.com/" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0"

[2026-11-10 13:25:10,951] ERROR in app: Exception on / [GET]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:25:10 +0000] "GET / HTTP/1.1" 500 265 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0"

[2026-11-10 13:25:12,106] ERROR in app: Exception on / [GET]

Traceback (most recent call last):

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 1511, in wsgi_app

    response = self.full_dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 919, in full_dispatch_request

    rv = self.handle_user_exception(e)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 917, in full_dispatch_request

    rv = self.dispatch_request()

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/app.py", line 902, in dispatch_request

    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]

           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^

  File "/opt/render/project/src/app.py", line 325, in home

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 150, in render_template

    template = app.jinja_env.get_or_select_template(template_name_or_list)

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1087, in get_or_select_template

    return self.get_template(template_name_or_list, parent, globals)

           ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 1016, in get_template

    return self._load_template(name, globals)

           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/environment.py", line 975, in _load_template

    template = self.loader.load(self, name, self.make_globals(globals))

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/jinja2/loaders.py", line 126, in load

    source, filename, uptodate = self.get_source(environment, name)

                                 ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 66, in get_source

    return self._get_source_fast(environment, template)

           ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^

  File "/opt/render/project/src/.venv/lib/python3.14/site-packages/flask/templating.py", line 100, in _get_source_fast

    raise TemplateNotFound(template)

jinja2.exceptions.TemplateNotFound: home.html

127.0.0.1 - - [10/Nov/2026:13:25:12 +0000] "GET / HTTP/1.1" 500 265 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36 Edg/157.0.0.0"

==> Detected service running on port 10000

==> Docs on specifying a port: https://render.com/docs/web-services#port-binding....THIS IS WHAT I FOUND

The log error points directly to the issue: jinja2.exceptions.TemplateNotFound: home.html.

This happens because Git and Render are looking for a folder named lowercase templates, but if your folder is capitalized as Templates (with a capital T), Linux servers on Render treat it as completely different, so Flask can't find your HTML files.

Let's fix this in your VS Code terminal right now:

1
Rename Templates Folder to Lowercase
Run this command in your VS Code terminal to rename the folder so Linux recognizes it:

Bash
git mv Templates templates
Verification: The terminal moves and renames the folder. (If it says the folder is already lowercase or git handles it, proceed to commit).

2
Commit and Push the Fix
Run these commands to send the updated folder name to GitHub:

Bash
git commit -m "Fix templates folder case sensitivity for Render"
git push origin main
Verification: The terminal uploads the change to GitHub, and Render will automatically trigger a new deployment.

Wait about 1 minute for Render to finish building the automatic deploy, then refresh your live app page ([https://spendwise-t4qq.onrender.com](https://spendwise-t4qq.onrender.com))! Let me know when it opens up.

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git mv Templates templates

fatal: renaming 'Templates' to 'templates/Templates' failed: Invalid argument

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git commit -m "Fix templates folder case sensitivity for Render"

>> git push origin main

On branch main

nothing to commit, working tree clean

info: please complete authentication in your browser...

Everything up-to-date

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> 

Because Windows treats Templates and templates as the exact same folder name, Git on Windows gets confused when trying to rename them directly. Linux servers like Render do care about uppercase letters, so we have to use a temporary folder name to force Git to update it.

Run these commands one by one in your VS Code terminal:

1
Move to a Temporary Folder Name
Run this command to temporarily rename the folder:

Bash
git mv Templates temp_folder
git commit -m "Rename to temp folder"
Verification: Git successfully moves the files into temp_folder and commits the change.

2
Rename to Lowercase 'templates'
Run this command to rename it to the lowercase folder name that Flask and Render expect:

Bash
git mv temp_folder templates
git commit -m "Rename templates folder to lowercase"
Verification: Git renames the folder correctly to lowercase templates.

3
Push Changes to GitHub
Push your updated folder structure to GitHub:

Bash
git push origin main
Verification: The terminal uploads the changes. Render will automatically pick up the fix, trigger a fresh build, and your app will load properly!

CANT I JUST CHANGE THE NAME ON THE NORMAL SECTION OF VS CODE

Yes, absolutely! Since Windows treats Templates and templates as the exact same name, you can bypass Git's confusion entirely by renaming it directly inside the VS Code editor sidebar.

1
Rename the Folder in VS Code Sidebar
Look at your file explorer sidebar on the left side of VS Code.

Right-click on the folder named Templates (with a capital T).

Click Rename and change it to lowercase templates (with a small t), then press Enter.
Verification: The folder name in your sidebar turns lowercase (templates).

2
Commit and Push the Change
Open your VS Code terminal and run these commands to send the updated folder name to GitHub:

Bash
git add -A
git commit -m "Rename Templates folder to lowercase templates"
git push origin main
Verification: The terminal uploads the changes successfully. Render will automatically pick it up, trigger a fresh build, and your app will load properly without the Internal Server Error!

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git add -A

>> git commit -m "Rename Templates folder to lowercase templates"

>> git push origin main

On branch main

nothing to commit, working tree clean

Everything up-to-date

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> 

Yes! Doing it directly inside VS Code's sidebar is the cleanest and easiest way to bypass Windows' case-insensitivity.

Since Git is currently showing your working tree as clean, it means the rename hasn't been staged or committed yet. Let's make sure Git catches the lowercase folder change right now:

1
Stage and Commit the Folder Rename
Run this command in your terminal to force Git to register the uppercase-to-lowercase folder change:

Bash
git add -A
git commit -m "Rename Templates to lowercase templates"
Verification: The terminal shows files being updated and committed.

2
Push to GitHub
Send the fixed folder structure up to GitHub:

Bash
git push origin main
Verification: The terminal outputs writing objects and confirms success.

Once that's pushed, Render will automatically pick up the update and deploy your app. Give it about 1 minute, refresh your live app page ([https://spendwise-t4qq.onrender.com](https://spendwise-t4qq.onrender.com)), and your Internal Server Error will be completely gone!

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git add -A

>> git commit -m "Rename Templates to lowercase templates"

On branch main

nothing to commit, working tree clean

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git push origin main

Everything up-to-date

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> 

Since Windows ignores letter casing in folder names, Git still thinks your local folder is capitalized as Templates, which is why it shows "nothing to commit" even after you renamed it in the sidebar. We can force Git to recognize the change by running a quick command in your terminal.

1
Configure Git to Track Letter Casing
Run this command in your VS Code terminal to force Git to care about uppercase vs lowercase letters:

Bash
git config core.ignorecase false
Verification: The terminal runs without any error messages.

2
Stage, Commit, and Push the Lowercase Folder
Now run these commands to properly log the folder rename and send it to GitHub:

Bash
git add -A
git commit -m "Force lowercase templates folder"
git push origin main
Verification: The terminal shows files being updated and successfully pushed to GitHub.

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git config core.ignorecase false

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> git add -A

>> git commit -m "Force lowercase templates folder"

>> git push origin main

[main 9fb7e05] Force lowercase templates folder

 10 files changed, 947 insertions(+)

 create mode 100644 templates/admin_blog.html

 create mode 100644 templates/base.html

 create mode 100644 templates/blog.html

 create mode 100644 templates/budgets.html

 create mode 100644 templates/clear_prompt.html

 create mode 100644 templates/expenses.html

 create mode 100644 templates/home.html

 create mode 100644 templates/index.html

 create mode 100644 templates/reports.html

 create mode 100644 templates/savings.html

Enumerating objects: 3, done.

Counting objects: 100% (3/3), done.

Delta compression using up to 8 threads

Compressing objects: 100% (2/2), done.

Writing objects: 100% (2/2), 258 bytes | 258.00 KiB/s, done.

Total 2 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)

remote: Resolving deltas: 100% (1/1), completed with 1 local object.

To https://github.com/blessingonyinye123/SpendWise.git

   7b6d176..9fb7e05  main -> main

PS C:\Users\Owner\Desktop\EXPENSE_TRACKER> 

Look at that output! It pushed successfully to GitHub! (7b6d176..9fb7e05 main -> main).

Render is now automatically picking up your new commit with the correctly cased lowercase templates folder.

1
Wait for Render Deployment
Give Render about 1 minute to finish building this latest commit. You can watch it in your Render dashboard under the Deploys tab.
Verification: The status turns to a green Live with your new commit hash (9fb7e05).

2
Test Your Live App
Once it turns live, refresh your browser tab at [https://spendwise-t4qq.onrender.com](https://spendwise-t4qq.onrender.com).
Verification: The "Internal Server Error" is completely gone, and your SpendWise application homepage loads successfully!

i have seen the app. but i noticed that the link i will share to others can make them set their names by themselves, and add the blog post i told you that i should be the only one adding

That is a very important security catch! Right now, because your application is live on the public web, anyone who visits the link can access the admin or blog creation routes if the URLs aren't protected.

To fix this so that only you can add blog posts or manage administrative settings, we need to add a secure login or admin passcode check to those specific routes in your app.py file.

Let's do this step by step:

1
Choose an Admin Protection Method
We can protect your admin/blog routes using one of two simple ways:

Option A (Secret Passcode): Visitors can view your expense tracker normally, but clicking the blog or admin section will ask for a secret password/passcode that only you know.

Option B (Admin Login Page): A dedicated login form where you enter a username and password before getting access to create posts.

2
Tell Me Your Preference
Would you prefer a quick secret passcode prompt or a proper login page for your admin dashboard? Once you let me know, we will update your code together so your blog stays strictly yours!

no. these two things i mentioned should only be done by me, the app should set their names to hello "name" when they log in to the site, not them setting their names by themselves. and they should see only a writen blog post, they cant edit or write

That makes complete sense! Let's break down how we will lock down those two parts so your app works exactly how you want:

Read-Only Blog for Visitors: Regular visitors will only see a clean page to read the blog posts you publish. All the buttons, forms, and options to write or edit posts will be hidden from them and moved to a secure admin page that only you can access.

Automatic "Hello [Name]" Greeting: Instead of letting users type or change their own display names manually, the app will automatically fetch their registered account name when they log in and greet them with "Hello [Name]" on their dashboard.

To make this happen, we need to update how your routes and HTML files handle permissions in app.py.

Would you like us to start with securing the Blog page first so visitors can only read posts, or would you like to set up the User Login Greeting first? Let me know which one you want to tackle right now!

lets do blog page first

Starting with the blog page is a brilliant first step!

To make the blog read-only for regular visitors while keeping the writing power exclusively in your hands, we are going to divide your blog into two clear parts:

The Public Blog Page (/blog): Visitors will only see a clean list of the posts you have published. There will be no forms, no input boxes, and no create/edit buttons visible to them.

The Admin Blog Page: This is a separate, protected route that only you can access to write, edit, or publish new posts.

Let's look at how your code is set up right now.

1
Check Your Blog Routes in app.py
Open your app.py file in VS Code.

Scroll down or search for your blog route (it usually starts with @app.route('/blog')).
Verification: You can see how your blog function currently fetches posts and passes them to your HTML template.

2
Check the HTML Template
Open your templates/blog.html file.

Check if there are any <form> tags, textareas, or submit buttons used for writing posts right inside that file.
Verification: You spot whether the writing form is currently sitting directly on the public blog page.

Tell me what you see inside your blog.html file—does it currently contain a form for writing posts, or is it just displaying existing posts?

{% extends "base.html" %}

{% block title %}Financial Guide & Blog - SpendWise{% endblock %}

{% block content %}

<div style="display: flex; flex-direction: column; gap: 24px;">



    <!-- Header Card -->

    <div class="card" style="background: linear-gradient(135deg, #4f46e5 0%, #818cf8 100%); color: white;">

        <h2 style="color: white; margin-bottom: 5px;">📖 Financial Guide & Blog</h2>

        <p style="margin: 0; opacity: 0.9;">Expert insights, money tips, and educational guides to help you master your expenses.</p>

    </div>



    <!-- Blog Posts List with Images -->

    {% if posts %}

        <div style="display: flex; flex-direction: column; gap: 20px;">

            {% for post in posts %}

            <div class="card" style="padding: 0; overflow: hidden;">

                {% if post[3] %}

                <div style="width: 100%; max-height: 300px; overflow: hidden; background: #000;">

                    <img src="{{ post[3] }}" alt="{{ post[1] }}" style="width: 100%; height: 100%; object-fit: cover;">

                </div>

                {% endif %}

                <div style="padding: 24px;">

                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">

                        <h3 style="margin: 0; color: var(--primary); font-size: 1.3rem;">{{ post[1] }}</h3>

                        <span style="font-size: 0.85rem; color: var(--text-light);">📅 {{ post[4] }}</span>

                    </div>

                    <p style="color: var(--text); line-height: 1.6; white-space: pre-wrap; margin-top: 10px;">{{ post[2] }}</p>

                </div>

            </div>

            {% endfor %}

        </div>

    {% else %}

        <div class="card" style="text-align: center; padding: 40px; color: var(--text-light);">

            <p style="font-style: italic; font-size: 1.05rem;">No educational articles published yet. Check back soon for money tips!</p>

        </div>

    {% endif %}



</div>

{% endblock %}...this is my blog.html

That blog.html template is already 100% read-only and clean!

Looking at your code, it only loops through and displays the posts (post[1], post[2], post[3], post[4]) with zero forms, buttons, or input boxes for writing. Regular visitors can only read what is there.

Since you already have an admin_blog.html file in your project for writing posts, let's look at how your app.py handles the blog routes so we can make sure the writing part is locked down exclusively to you.

Can you check your app.py file and show me the lines around your blog routes (usually starting with @app.route('/blog') and any admin blog routes)?

@app.before_request

def before_request():

    if 'currency' not in session:

        session['currency'] = '₦'

    if 'user_name' not in session:

        session['user_name'] = 'Ikeli'



@app.route("/set_currency", methods=["POST"])

def set_currency():

    selected_currency = request.form.get("currency")

    if selected_currency in CURRENCIES:

        session['currency'] = selected_currency

    return redirect(request.referrer or url_for('home'))



@app.route("/set_name", methods=["POST"])

def set_name():

    name = request.form.get("user_name")

    if name:

        session['user_name'] = name.title()

    return redirect(request.referrer or url_for('home'))



@app.route("/")

def home():

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/dashboard")

def index():

    expenses = database.get_expenses()

    total = database.get_total_spending()

    raw_budgets = database.get_budgets()

    goals = database.get_savings_goals()

   

    day_of_year = datetime.datetime.now().timetuple().tm_yday

    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]

   

    budgets = []

    for cat, limit in raw_budgets:

        spent = database.get_category_spending(cat)

        remaining = limit - spent

        percentage = (spent / limit * 100) if limit > 0 else 0

        budgets.append({

            "category": cat,

            "limit": limit,

            "spent": spent,

            "remaining": remaining,

            "percentage": round(percentage, 1)

        })

       

    return render_template("index.html", total=total, budgets=budgets, goals=goals, expenses=expenses[:5],

                           currency=session.get('currency', '₦'), currencies=CURRENCIES, daily_tip=daily_tip)



@app.route("/expenses")

def expenses_page():

    expenses = database.get_expenses()

    total = database.get_total_spending()

    return render_template("expenses.html", expenses=expenses, total=total,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/budgets")

def budgets_page():

    raw_budgets = database.get_budgets()

    budgets = []

    for cat, limit in raw_budgets:

        spent = database.get_category_spending(cat)

        remaining = limit - spent

        percentage = (spent / limit * 100) if limit > 0 else 0

        budgets.append({

            "category": cat,

            "limit": limit,

            "spent": spent,

            "remaining": remaining,

            "percentage": round(percentage, 1)

        })

    return render_template("budgets.html", budgets=budgets,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/savings")

def savings_page():

    goals = database.get_savings_goals()

    return render_template("savings.html", goals=goals,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/reports")

def reports_page():

    daily_summary = database.get_daily_summary()

    monthly_summary = database.get_monthly_summary()

    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/blog")

def blog_page():

    posts = database.get_blog_posts()

    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/admin/blog", methods=["GET", "POST"])

def admin_blog():

    if request.method == "POST":

        title = request.form.get("title")

        content = request.form.get("content")

        image_url = request.form.get("image_url")

        date = request.form.get("date")

        database.add_blog_post(title, content, image_url, date)

        return redirect(url_for("blog_page"))

    posts = database.get_blog_posts()

    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/admin/blog/delete/<int:post_id>")

def delete_blog(post_id):

    database.delete_blog_post(post_id)

    return redirect(url_for("admin_blog"))



@app.route("/add", methods=["POST"])

def add():

    title = request.form.get("title").title()

    amount = float(request.form.get("amount"))

    category = request.form.get("category").title()

    date = request.form.get("date")

    database.add_expense(title, amount, category, date)

    return redirect(url_for("expenses_page"))



@app.route("/set_budget", methods=["POST"])

def set_budget():

    category = request.form.get("category").title()

    limit_amount = float(request.form.get("limit_amount"))

    database.set_budget(category, limit_amount)

    return redirect(url_for("budgets_page"))



@app.route("/add_goal", methods=["POST"])

def add_goal():

    name = request.form.get("name").title()

    target_amount = float(request.form.get("target_amount"))

    current_amount = float(request.form.get("current_amount") or 0.0)

    database.add_savings_goal(name, target_amount, current_amount)

    return redirect(url_for("savings_page"))



@app.route("/delete/<int:expense_id>")

def delete(expense_id):

    database.delete_expense(expense_id)

    return redirect(url_for("expenses_page"))



@app.route("/delete_budget/<string:category>")

def delete_budget(category):

    database.delete_budget(category)

    return redirect(url_for("budgets_page"))



@app.route("/delete_goal/<int:goal_id>")

def delete_goal(goal_id):

    database.delete_savings_goal(goal_id)

    return redirect(url_for("savings_page"))



@app.route("/clear_prompt")

def clear_prompt():

    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/execute_clear", methods=["POST"])

def execute_clear():

    choice = request.form.get("clear_budgets")

    database.clear_expenses()

    if choice == "yes":

        database.clear_budgets()

    return redirect(url_for("expenses_page"))



if __name__ == "__main__":

    app.run(debug=True)

To make your app secure and work exactly the way you want, we need to make two main updates to your app.py:

Lock Down the Blog: Protect the /admin/blog and delete routes so that only you can access them with a secret password, while regular visitors only see the clean, read-only /blog page.

Remove Manual Name Setting: Delete the /set_name route so visitors can no longer type or change their own names. Instead, the app will automatically greet standard users with a default welcome (like "Hello Friend" or "Hello Guest"), while keeping your owner greeting secure.

Here is how we update your app.py step by step:

Step 1: Remove Name Setting & Add Admin Protection in app.py
Open your app.py and replace your name-setting routes and blog admin routes with this secure version:

Python
@app.before_request
def before_request():
    if 'currency' not in session:
        session['currency'] = '₦'
    if 'user_name' not in session:
        # Default name for visitors (you can change this to Guest or Friend)
        session['user_name'] = 'Friend'

# NOTE: The /set_name route has been removed completely 
# so users cannot change their names manually!

@app.route("/blog")
def blog_page():
    posts = database.get_blog_posts()
    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

# --- SECURE ADMIN LOGIN & ROUTES ---

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        passcode = request.form.get("passcode")
        # Change 'mysecretpassword' to any secret password only you know!
        if passcode == "mysecretpassword": 
            session['is_admin'] = True
            session['user_name'] = 'Ikeli' # Automatically sets your owner name when logged in!
            return redirect(url_for("admin_blog"))
        else:
            return render_template("admin_login.html", error="Incorrect Passcode", currency=session.get('currency', '₦'), currencies=CURRENCIES)
    return render_template("admin_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog", methods=["GET", "POST"])
def admin_blog():
    # Check if you are logged in as admin
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
        
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image_url = request.form.get("image_url")
        date = request.form.get("date")
        database.add_blog_post(title, content, image_url, date)
        return redirect(url_for("blog_page"))
        
    posts = database.get_blog_posts()
    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog/delete/<int:post_id>")
def delete_blog(post_id):
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
    database.delete_blog_post(post_id)
    return redirect(url_for("admin_blog"))
What this code does for you:
Blocks Visitors from Writing: If anyone tries to type [yourwebsite.com/admin/blog](https://yourwebsite.com/admin/blog), the app checks if they have admin privileges. If they don't, it safely bounces them to a login page.

Removes Name Customization: Because the /set_name route is gone, visitors cannot change their displayed name. The app automatically handles greetings.

Protects Your Blog: Only when you visit /admin/login and type your secret password will you unlock the ability to write and delete blog posts.

Would you like help creating the simple admin_login.html template file so you have a clean login box for your secret password?

like i should replace all those codes i sent with these last one you just sent?

No, you don't need to replace your entire app.py file! You only need to swap out three specific parts:

Update the @app.before_request part at the top.

Delete the old @app.route("/set_name", methods=["POST"]) route completely.

Replace your old blog routes (/blog, /admin/blog, and /admin/blog/delete/...) with the new secure admin versions.

All your other routes (like /dashboard, /expenses, /budgets, /savings, etc.) should stay exactly where they are.

Here is how your app.py should look when you put those pieces together:

Python
@app.before_request
def before_request():
    if 'currency' not in session:
        session['currency'] = '₦'
    if 'user_name' not in session:
        session['user_name'] = 'Friend'  # Default greeting for regular visitors

@app.route("/set_currency", methods=["POST"])
def set_currency():
    selected_currency = request.form.get("currency")
    if selected_currency in CURRENCIES:
        session['currency'] = selected_currency
    return redirect(request.referrer or url_for('home'))

# NOTE: The /set_name route was removed here so users cannot change names manually!

@app.route("/")
def home():
    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/dashboard")
def index():
    expenses = database.get_expenses()
    total = database.get_total_spending()
    raw_budgets = database.get_budgets()
    goals = database.get_savings_goals()
    
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]
    
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
        
    return render_template("index.html", total=total, budgets=budgets, goals=goals, expenses=expenses[:5], 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES, daily_tip=daily_tip)

@app.route("/expenses")
def expenses_page():
    expenses = database.get_expenses()
    total = database.get_total_spending()
    return render_template("expenses.html", expenses=expenses, total=total, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/budgets")
def budgets_page():
    raw_budgets = database.get_budgets()
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
    return render_template("budgets.html", budgets=budgets, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/savings")
def savings_page():
    goals = database.get_savings_goals()
    return render_template("savings.html", goals=goals, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/reports")
def reports_page():
    daily_summary = database.get_daily_summary()
    monthly_summary = database.get_monthly_summary()
    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

# --- SECURE BLOG & ADMIN ROUTES ---

@app.route("/blog")
def blog_page():
    posts = database.get_blog_posts()
    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        passcode = request.form.get("passcode")
        if passcode == "mysecretpassword":  # You can change this password to anything you want!
            session['is_admin'] = True
            session['user_name'] = 'Ikeli'  # Automatically sets your owner name when you log in
            return redirect(url_for("admin_blog"))
        else:
            return render_template("admin_login.html", error="Incorrect Passcode", currency=session.get('currency', '₦'), currencies=CURRENCIES)
    return render_template("admin_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog", methods=["GET", "POST"])
def admin_blog():
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
        
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image_url = request.form.get("image_url")
        date = request.form.get("date")
        database.add_blog_post(title, content, image_url, date)
        return redirect(url_for("blog_page"))
        
    posts = database.get_blog_posts()
    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog/delete/<int:post_id>")
def delete_blog(post_id):
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
    database.delete_blog_post(post_id)
    return redirect(url_for("admin_blog"))

# --- ALL OTHER APP ROUTES REMAIN THE SAME ---

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title").title()
    amount = float(request.form.get("amount"))
    category = request.form.get("category").title()
    date = request.form.get("date")
    database.add_expense(title, amount, category, date)
    return redirect(url_for("expenses_page"))

@app.route("/set_budget", methods=["POST"])
def set_budget():
    category = request.form.get("category").title()
    limit_amount = float(request.form.get("limit_amount"))
    database.set_budget(category, limit_amount)
    return redirect(url_for("budgets_page"))

@app.route("/add_goal", methods=["POST"])
def add_goal():
    name = request.form.get("name").title()
    target_amount = float(request.form.get("target_amount"))
    current_amount = float(request.form.get("current_amount") or 0.0)
    database.add_savings_goal(name, target_amount, current_amount)
    return redirect(url_for("savings_page"))

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    database.delete_expense(expense_id)
    return redirect(url_for("expenses_page"))

@app.route("/delete_budget/<string:category>")
def delete_budget(category):
    database.delete_budget(category)
    return redirect(url_for("budgets_page"))

@app.route("/delete_goal/<int:goal_id>")
def delete_goal(goal_id):
    database.delete_savings_goal(goal_id)
    return redirect(url_for("savings_page"))

@app.route("/clear_prompt")
def clear_prompt():
    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/execute_clear", methods=["POST"])
def execute_clear():
    choice = request.form.get("clear_budgets")
    database.clear_expenses()
    if choice == "yes":
        database.clear_budgets()
    return redirect(url_for("expenses_page"))

if __name__ == "__main__":
    app.run(debug=True)
Once you update this in your app.py, we just need to create a tiny admin_login.html file so you have a box to type your secret password. Would you like me to write that quick HTML template for you?

after the random quotes..... then you see that code i sent, should i replace them with these last one you sent

Yes, exactly! You can copy that complete code block above and paste it right into your app.py file, replacing your old code. It has everything properly organized so your app runs smoothly, the name-setting form is removed, and your blog is safely locked behind your admin password.

Once you save your updated app.py file, the next step is to create the small login page template so you can log in as the owner.

Create a new file inside your templates/ folder named admin_login.html and paste this code into it:

HTML
{% extends "base.html" %}
{% block title %}Admin Login - SpendWise{% endblock %}
{% block content %}
<div style="max-width: 400px; margin: 40px auto;" class="card">
    <h2 style="color: var(--primary); margin-bottom: 20px; text-align: center;">🔐 Owner Login</h2>
    
    {% if error %}
    <div style="background: #fee2e2; color: #b91c1c; padding: 10px; border-radius: 6px; margin-bottom: 15px; text-align: center;">
        {{ error }}
    </div>
    {% endif %}

    <form method="POST" style="display: flex; flex-direction: column; gap: 15px;">
        <div>
            <label style="display: block; margin-bottom: 5px; font-weight: 500;">Admin Passcode:</label>
            <input type="password" name="passcode" required style="width: 100%; padding: 10px; border: 1px solid var(--border); border-radius: 6px;">
        </div>
        <button type="submit" style="background: var(--primary); color: white; padding: 10px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">
            Login to Admin
        </button>
    </form>
</div>
{% endblock %}
Once you have saved both files (app.py and admin_login.html), let me know and we can test it or push it up to Render!

done\

That is fantastic! Your app is now fully secured with your admin login and a clean, read-only blog for visitors.

Let's push these changes to GitHub so Render updates your live website:

1
Stage and Commit Your Changes
Open your VS Code terminal and run these commands to save your updates:

Bash
git add -A
git commit -m "Add admin login and secure blog routes"
Verification: The terminal shows files being updated and committed.

2
Push to GitHub
Send the updates to GitHub:

Bash
git push origin main
Verification: The terminal confirms the successful upload to GitHub.

Once Render finishes deploying (takes about 1 minute), you can visit your live app ([https://spendwise-t4qq.onrender.com](https://spendwise-t4qq.onrender.com)), go to /admin/login, type in your passcode (mysecretpassword), and you'll be all set to manage your blog as the exclusive owner! Let me know when it's live and if you're able to log in successfully.

lets do the name before that

Ah, yes! Let's handle the automatic greeting next so that regular users can't type or change their own names, but instead see a clean, automatic greeting like "Hello, Friend" (while you automatically get "Hello, Ikeli" when you log in as the owner).

To make this happen, we need to look at your header or navigation layout template—usually base.html—where that old name-setting box was located.

1
Check base.html for the Name Form
Open your templates/base.html file in VS Code.

Look for the section where users could type their name and submit it (it usually looks like a <form action="/set_name" method="POST">).
Verification: You find the form tag or input field used for changing the display name.

2
Share Your Header / Navigation Code
Copy and paste the navigation or header portion of your base.html file here, and we will update it together so it simply displays "Hello, [Name]" automatically without any input boxes!

<!DOCTYPE html>

<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%234f46e5%22 stroke-width=%222.5%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><path d=%22M3 17l6-6 4 4 8-8%22/><polyline points=%2214 7 21 7 21 14%22/></svg>">

    <title>{% block title %}SpendWise{% endblock %}</title>

    <style>

        :root {

            --primary: #4f46e5;

            --primary-hover: #4338ca;

            --bg: #f8fafc;

            --card-bg: #ffffff;

            --text: #0f172a;

            --text-light: #64748b;

            --danger: #ef4444;

            --border: #e2e8f0;

        }



        body {

            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;

            background-color: var(--bg);

            color: var(--text);

            margin: 0;

            padding: 0;

            display: flex;

            min-height: 100vh;

        }



        @keyframes fadeIn {

            from { opacity: 0; transform: translateY(12px); }

            to { opacity: 1; transform: translateY(0); }

        }



        @keyframes subtlePulse {

            0% { box-shadow: 0 0 0 0 rgba(79, 70, 229, 0.2); }

            70% { box-shadow: 0 0 0 10px rgba(79, 70, 229, 0); }

            100% { box-shadow: 0 0 0 0 rgba(79, 70, 229, 0); }

        }



        sidebar {

            width: 270px;

            background: var(--card-bg);

            border-right: 1px solid var(--border);

            display: flex;

            flex-direction: column;

            justify-content: space-between;

            padding: 28px 20px;

            position: fixed;

            height: 100vh;

            box-sizing: border-box;

            z-index: 100;

            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);

        }



        .sidebar-top {

            display: flex;

            flex-direction: column;

            gap: 30px;

        }



        .nav-brand {

            font-size: 1.35rem;

            font-weight: 800;

            color: var(--primary);

            text-decoration: none;

            display: flex;

            align-items: center;

            gap: 10px;

            letter-spacing: -0.5px;

        }



        .nav-brand svg {

            width: 28px;

            height: 28px;

            stroke: var(--primary);

            fill: none;

            transition: transform 0.3s ease;

        }



        .nav-brand:hover svg {

            transform: scale(1.15) rotate(-5deg);

        }



        .nav-links {

            display: flex;

            flex-direction: column;

            gap: 6px;

        }



        .nav-links a {

            text-decoration: none;

            color: var(--text-light);

            font-weight: 600;

            font-size: 0.93rem;

            padding: 11px 14px;

            border-radius: 10px;

            transition: all 0.25s ease;

            display: flex;

            align-items: center;

            gap: 10px;

        }



        .nav-links a:hover {

            color: var(--primary);

            background: #eef2ff;

            transform: translateX(4px);

        }



        .sidebar-footer {

            display: flex;

            flex-direction: column;

            gap: 14px;

            border-top: 1px solid var(--border);

            padding-top: 20px;

        }



        .currency-form select {

            padding: 9px 12px;

            border-radius: 8px;

            border: 1px solid var(--border);

            background: #f8fafc;

            font-weight: 600;

            color: var(--primary);

            outline: none;

            width: 100%;

        }



        .admin-link {

            font-size: 0.82rem;

            color: var(--text-light);

            text-decoration: none;

            text-align: center;

            font-weight: 500;

            transition: color 0.2s;

        }



        .admin-link:hover {

            color: var(--primary);

        }



        .main-content {

            margin-left: 270px;

            flex: 1;

            padding: 40px;

            box-sizing: border-box;

            max-width: 1200px;

            animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);

        }



        .card {

            background: var(--card-bg);

            border-radius: 16px;

            box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.04);

            padding: 30px;

            margin-bottom: 28px;

            border: 1px solid var(--border);

            transition: transform 0.25s ease, box-shadow 0.25s ease;

        }



        .card:hover {

            transform: translateY(-2px);

            box-shadow: 0 10px 25px -4px rgba(0, 0, 0, 0.06);

        }



        h2, h3 {

            margin-top: 0;

            color: var(--text);

        }



        button {

            background-color: var(--primary);

            color: white;

            border: none;

            padding: 11px 22px;

            border-radius: 10px;

            font-weight: 600;

            cursor: pointer;

            transition: all 0.2s ease;

        }



        button:hover {

            background-color: var(--primary-hover);

            transform: translateY(-1px);

            box-shadow: 0 4px 12px rgba(79, 70, 229, 0.25);

        }



        input, select, textarea {

            padding: 11px 14px;

            border: 1px solid var(--border);

            border-radius: 10px;

            font-size: 0.95rem;

            outline: none;

            width: 100%;

            box-sizing: border-box;

            font-family: inherit;

            background: #fff;

            transition: border-color 0.2s, box-shadow 0.2s;

        }



        input:focus, select:focus, textarea:focus {

            border-color: var(--primary);

            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.12);

        }



        table {

            width: 100%;

            border-collapse: collapse;

            text-align: left;

            margin-top: 15px;

        }



        th, td {

            padding: 14px 18px;

            border-bottom: 1px solid var(--border);

        }



        th {

            font-weight: 600;

            color: var(--text-light);

            background-color: #f8fafc;

            font-size: 0.88rem;

            text-transform: uppercase;

        }



        .badge {

            background-color: #eef2ff;

            color: var(--primary);

            padding: 5px 12px;

            border-radius: 20px;

            font-size: 0.83rem;

            font-weight: 600;

        }



        @media (max-width: 900px) {

            body { flex-direction: column; }

            sidebar {

                position: relative;

                width: 100%;

                height: auto;

                border-right: none;

                border-bottom: 1px solid var(--border);

                padding: 20px;

            }

            .sidebar-top { gap: 18px; }

            .nav-links { flex-direction: row; flex-wrap: wrap; gap: 8px; }

            .nav-links a { padding: 8px 12px; font-size: 0.85rem; }

            .main-content { margin-left: 0; padding: 20px 16px; max-width: 100%; }

        }

    </style>

    {% block extra_head %}{% endblock %}

</head>

<body>



    <sidebar>

        <div class="sidebar-top">

            <a href="/" class="nav-brand">

                <svg viewBox="0 0 24 24" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">

                    <path d="M3 17l6-6 4 4 8-8"/>

                    <polyline points="14 7 21 7 21 14"/>

                </svg>

                SpendWise

            </a>

            <div class="nav-links">

                <a href="/">🏠 Home</a>

                <a href="/dashboard">📊 Dashboard</a>

                <a href="/expenses">💸 Expenses</a>

                <a href="/budgets">🎯 Budgets</a>

                <a href="/savings">💰 Savings Goals</a>

                <a href="/reports">📈 Reports</a>

                <a href="/blog">📖 Financial Guide & Blog</a>

            </div>

        </div>



        <div class="sidebar-footer">

            <form action="/set_currency" method="POST" class="currency-form">

                <select name="currency" onchange="this.form.submit()">

                    {% for code, name in currencies.items() %}

                        <option value="{{ code }}" {% if currency == code %}selected{% endif %}>{{ code }} - {{ name.split(' ')[0] }}</option>

                    {% endfor %}

                </select>

            </form>



            <form action="/set_name" method="POST" style="display: flex; gap: 6px;">

                <input type="text" name="user_name" value="{{ session.get('user_name', 'Ikeli') }}" placeholder="Your Name" style="padding: 7px 10px; font-size: 0.85rem; border-radius: 8px;">

                <button type="submit" style="padding: 7px 12px; font-size: 0.85rem; border-radius: 8px;">Set</button>

            </form>



            <a href="/admin/blog" class="admin-link">🔒 Admin Article Portal</a>

        </div>

    </sidebar>



    <div class="main-content">

        {% block content %}{% endblock %}

    </div>



    <script>

        document.addEventListener("DOMContentLoaded", function() {

            let dateInput = document.querySelector('input[type="date"]');

            if (dateInput && !dateInput.value) {

                dateInput.value = new Date().toISOString().split('T')[0];

            }

        });



        function confirmDelete(event, itemName) {

            if (!confirm(`Are you sure you want to permanently delete "${itemName}"?`)) {

                event.preventDefault();

            }

        }

    </script>

</body>

</html>

To replace the manual name-setting box with an automatic greeting (showing "Hello, Ikeli" when you are logged in as admin, or "Hello, Friend" for regular visitors), we will replace that bottom form with a clean badge.

Update templates/base.html
Find this section in your templates/base.html file (near the bottom of the sidebar):

HTML
            <form action="/set_name" method="POST" style="display: flex; gap: 6px;">
                <input type="text" name="user_name" value="{{ session.get('user_name', 'Ikeli') }}" placeholder="Your Name" style="padding: 7px 10px; font-size: 0.85rem; border-radius: 8px;">
                <button type="submit" style="padding: 7px 12px; font-size: 0.85rem; border-radius: 8px;">Set</button>
            </form>
Replace those lines with this clean greeting badge:

HTML
            <div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center;">
                👋 Hello, {{ session.get('user_name', 'Friend') }}
            </div>
Push Your Final Changes to Render
Open your VS Code terminal and push your updated files to GitHub so everything is live:

Bash
git add -A
git commit -m "Replace manual name input with automatic greeting badge"
git push origin main
Once Render completes the build, your app will automatically greet visitors as "Hello, Friend" and greet you as "Hello, Ikeli" whenever you log in as the owner, keeping your blog fully read-only for everyone else!

<div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center;">

                👋 Hello, {{ session.get('user_name', 'Friend') }}

            </div>......DID YOU SAY FRIEND? I SAID DO IT SO THAT IF THEY LOG IN TO THE PAGE WITH THEIR NAME, IT WILL BE THEIR NAMES DISPLAYED THERE. HOW ABOUT A LOG IN SESSION

Ah, I understand completely now! You want regular visitors to be able to enter their own name when they visit or log into the site, so it personally greets them with "Hello, [Their Name]", while your owner account greets you as "Hello, Ikeli".

Instead of a bulky input box cluttering the sidebar, we can use a quick, clean Login / Welcome modal or form when they first arrive, or keep a simple name-entry prompt that saves their name into their session securely without letting them write or edit your blog.

Let's set up a proper user session login so that:

Visitors can enter their name once when they start using the app.

The app stores their name in their session and displays "Hello, [Their Name]".

Your admin login stays completely separate and secure.

Here is how we update app.py and base.html to make user logins seamless:

1. Update app.py with a User Login Route
Add this simple user login route to your app.py so visitors can set their name when they arrive:

Python
@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        name = request.form.get("user_name")
        if name:
            session['user_name'] = name.title()
        return redirect(url_for('home'))
    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)
(And make sure your before_request defaults to "Friend" if they haven't logged in yet).

2. Update templates/base.html Sidebar
In your sidebar footer, replace the greeting badge with a link to log in or switch names if they haven't yet:

HTML
            <div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center; display: flex; justify-content: space-between; align-items: center;">
                <span>👋 Hello, {{ session.get('user_name', 'Friend') }}</span>
                <a href="/login" style="font-size: 0.75rem; color: var(--primary); text-decoration: underline;">Change</a>
            </div>
3. Create templates/user_login.html
Create a clean login page where users enter their name:

HTML
{% extends "base.html" %}
{% block title %}Welcome - SpendWise{% endblock %}
{% block content %}
<div style="max-width: 400px; margin: 40px auto;" class="card">
    <h2 style="color: var(--primary); margin-bottom: 10px; text-align: center;">Welcome to SpendWise</h2>
    <p style="color: var(--text-light); text-align: center; margin-bottom: 20px; font-size: 0.9rem;">Please enter your name to personalize your experience.</p>

    <form method="POST" style="display: flex; flex-direction: column; gap: 15px;">
        <div>
            <label style="display: block; margin-bottom: 5px; font-weight: 500;">Your Name:</label>
            <input type="text" name="user_name" required placeholder="e.g. Sarah" style="width: 100%; padding: 10px; border: 1px solid var(--border); border-radius: 6px;">
        </div>
        <button type="submit" style="background: var(--primary); color: white; padding: 10px; border: none; border-radius: 6px; font-weight: 600; cursor: pointer;">
            Continue to SpendWise
        </button>
    </form>
</div>
{% endblock %}
This way, regular users get their own personalized "Hello, [Their Name]" greeting stored safely in their session, while your admin privileges and blog writing remain locked strictly to you!

done. i added them as under the last codes

That is brilliant! By setting up the user login session this way, anyone who visits can enter their name and see their own personalized "Hello, [Their Name]" greeting, while your admin dashboard and blog-writing capabilities remain completely locked behind your secure owner password.

Let's save and push these final updates to Render so everything is live and fully tested:

1
Stage and Commit Your Changes
Open your VS Code terminal and run these commands:

Bash
git add -A
git commit -m "Add personalized user login session and greeting badge"
Verification: The terminal successfully stages and commits all your new changes.

2
Push to GitHub
Send your code to GitHub:

Bash
git push origin main
Verification: The terminal pushes the updates, and Render automatically triggers a fresh build.

Give Render about 1 minute to deploy. Once it's live, visit your site, test logging in with a visitor name to see your customized greeting, and try your admin route (/admin/login) with your passcode to verify your blog management is fully secure!

<script>

        document.addEventListener("DOMContentLoaded", function() {

            let dateInput = document.querySelector('input[type="date"]');

            if (dateInput && !dateInput.value) {

                dateInput.value = new Date().toISOString().split('T')[0];

            }

        });



        function confirmDelete(event, itemName) {

            if (!confirm(`Are you sure you want to permanently delete "${itemName}"?`)) {

                event.preventDefault();

            }

        }

    </script>

    <div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center; display: flex; justify-content: space-between; align-items: center;">

                <span>👋 Hello, {{ session.get('user_name', 'Friend') }}</span>

                <a href="/login" style="font-size: 0.75rem; color: var(--primary); text-decoration: underline;">Change</a>

            </div>

</body>

</html>....this is the last part of my base.html.... is it correct?

Checking the tail end of your base.html file, there is one tiny structural fix needed!

Right now, your script block comes before that greeting div, but both of them are placed after the closing </body> tag. In HTML, everything—including your scripts and footer badges—needs to sit neatly inside the body before it closes.

Here is how the exact bottom of your base.html should look so it is 100% valid HTML:

HTML
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            let dateInput = document.querySelector('input[type="date"]');
            if (dateInput && !dateInput.value) {
                dateInput.value = new Date().toISOString().split('T')[0];
            }
        });

        function confirmDelete(event, itemName) {
            if (!confirm(`Are you sure you want to permanently delete "${itemName}"?`)) {
                event.preventDefault();
            }
        }
    </script>
</body>
</html>
Wait—where does the greeting badge go then? The greeting badge actually belongs inside your sidebar footer in base.html (right above or next to where your admin portal link is), not at the very bottom of the entire page!

Let's place it correctly inside your sidebar footer:

HTML
        <div class="sidebar-footer">
            <form action="/set_currency" method="POST" class="currency-form">
                <select name="currency" onchange="this.form.submit()">
                    {% for code, name in currencies.items() %}
                        <option value="{{ code }}" {% if currency == code %}selected{% endif %}>{{ code }} - {{ name.split(' ')[0] }}</option>
                    {% endfor %}
                </select>
            </form>

            <div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center; display: flex; justify-content: space-between; align-items: center;">
                <span>👋 Hello, {{ session.get('user_name', 'Friend') }}</span>
                <a href="/login" style="font-size: 0.75rem; color: var(--primary); text-decoration: underline;">Change</a>
            </div>

            <a href="/admin/blog" class="admin-link">🔒 Admin Article Portal</a>
        </div>
Make sure that greeting div is nested inside the <div class="sidebar-footer"> container, keep your script right above </body>, and your HTML structure will be completely clean and error-free!

i dont know where to place it

No problem at all! Let's make it super easy.

You can replace your entire templates/base.html code with this clean, complete version below. It has the sidebar footer greeting placed in the correct spot and everything structured properly:

HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22 fill=%22none%22 stroke=%22%234f46e5%22 stroke-width=%222.5%22 stroke-linecap=%22round%22 stroke-linejoin=%22round%22><path d=%22M3 17l6-6 4 4 8-8%22/><polyline points=%2214 7 21 7 21 14%22/></svg>">
    <title>{% block title %}SpendWise{% endblock %}</title>
    <style>
        :root {
            --primary: #4f46e5;
            --primary-hover: #4338ca;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text: #0f172a;
            --text-light: #64748b;
            --danger: #ef4444;
            --border: #e2e8f0;
        }

        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            background-color: var(--bg);
            color: var(--text);
            margin: 0;
            padding: 0;
            display: flex;
            min-height: 100vh;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        }

        sidebar {
            width: 270px;
            background: var(--card-bg);
            border-right: 1px solid var(--border);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding: 28px 20px;
            position: fixed;
            height: 100vh;
            box-sizing: border-box;
            z-index: 100;
        }

        .sidebar-top {
            display: flex;
            flex-direction: column;
            gap: 30px;
        }

        .nav-brand {
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--primary);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
            letter-spacing: -0.5px;
        }

        .nav-brand svg {
            width: 28px;
            height: 28px;
            stroke: var(--primary);
            fill: none;
            transition: transform 0.3s ease;
        }

        .nav-brand:hover svg {
            transform: scale(1.15) rotate(-5deg);
        }

        .nav-links {
            display: flex;
            flex-direction: column;
            gap: 6px;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-light);
            font-weight: 600;
            font-size: 0.93rem;
            padding: 11px 14px;
            border-radius: 10px;
            transition: all 0.25s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .nav-links a:hover {
            color: var(--primary);
            background: #eef2ff;
            transform: translateX(4px);
        }

        .sidebar-footer {
            display: flex;
            flex-direction: column;
            gap: 14px;
            border-top: 1px solid var(--border);
            padding-top: 20px;
        }

        .currency-form select {
            padding: 9px 12px;
            border-radius: 8px;
            border: 1px solid var(--border);
            background: #f8fafc;
            font-weight: 600;
            color: var(--primary);
            outline: none;
            width: 100%;
        }

        .admin-link {
            font-size: 0.82rem;
            color: var(--text-light);
            text-decoration: none;
            text-align: center;
            font-weight: 500;
            transition: color 0.2s;
        }

        .admin-link:hover {
            color: var(--primary);
        }

        .main-content {
            margin-left: 270px;
            flex: 1;
            padding: 40px;
            box-sizing: border-box;
            max-width: 1200px;
            animation: fadeIn 0.4s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .card {
            background: var(--card-bg);
            border-radius: 16px;
            box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.04);
            padding: 30px;
            margin-bottom: 28px;
            border: 1px solid var(--border);
        }

        input, select, textarea {
            padding: 11px 14px;
            border: 1px solid var(--border);
            border-radius: 10px;
            font-size: 0.95rem;
            outline: none;
            width: 100%;
            box-sizing: border-box;
            background: #fff;
        }

        @media (max-width: 900px) {
            body { flex-direction: column; }
            sidebar {
                position: relative;
                width: 100%;
                height: auto;
                border-right: none;
                border-bottom: 1px solid var(--border);
                padding: 20px;
            }
            .main-content { margin-left: 0; padding: 20px 16px; max-width: 100%; }
        }
    </style>
    {% block extra_head %}{% endblock %}
</head>
<body>

    <sidebar>
        <div class="sidebar-top">
            <a href="/" class="nav-brand">
                <svg viewBox="0 0 24 24" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 17l6-6 4 4 8-8"/>
                    <polyline points="14 7 21 7 21 14"/>
                </svg>
                SpendWise
            </a>
            <div class="nav-links">
                <a href="/">🏠 Home</a>
                <a href="/dashboard">📊 Dashboard</a>
                <a href="/expenses">💸 Expenses</a>
                <a href="/budgets">🎯 Budgets</a>
                <a href="/savings">💰 Savings Goals</a>
                <a href="/reports">📈 Reports</a>
                <a href="/blog">📖 Financial Guide & Blog</a>
            </div>
        </div>

        <div class="sidebar-footer">
            <form action="/set_currency" method="POST" class="currency-form">
                <select name="currency" onchange="this.form.submit()">
                    {% for code, name in currencies.items() %}
                        <option value="{{ code }}" {% if currency == code %}selected{% endif %}>{{ code }} - {{ name.split(' ')[0] }}</option>
                    {% endfor %}
                </select>
            </form>

            <div style="background: #eef2ff; color: var(--primary); padding: 9px 12px; border-radius: 8px; font-size: 0.88rem; font-weight: 600; text-align: center; display: flex; justify-content: space-between; align-items: center;">
                <span>👋 Hello, {{ session.get('user_name', 'Friend') }}</span>
                <a href="/login" style="font-size: 0.75rem; color: var(--primary); text-decoration: underline;">Change</a>
            </div>

            <a href="/admin/blog" class="admin-link">🔒 Admin Article Portal</a>
        </div>
    </sidebar>

    <div class="main-content">
        {% block content %}{% endblock %}
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            let dateInput = document.querySelector('input[type="date"]');
            if (dateInput && !dateInput.value) {
                dateInput.value = new Date().toISOString().split('T')[0];
            }
        });

        function confirmDelete(event, itemName) {
            if (!confirm(`Are you sure you want to permanently delete "${itemName}"?`)) {
                event.preventDefault();
            }
        }
    </script>
</body>
</html>
Just paste this directly into your templates/base.html file, save it, and you'll be completely set to push and deploy!

done. @app.route("/clear_prompt")

def clear_prompt():

    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/execute_clear", methods=["POST"])

def execute_clear():

    choice = request.form.get("clear_budgets")

    database.clear_expenses()

    if choice == "yes":

        database.clear_budgets()

    return redirect(url_for("expenses_page"))



if __name__ == "__main__":

    app.run(debug=True)



@app.route("/login", methods=["GET", "POST"])

def user_login():

    if request.method == "POST":

        name = request.form.get("user_name")

        if name:

            session['user_name'] = name.title()

        return redirect(url_for('home'))

    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)... this is the last seciton of my app.py

That bottom section of your app.py has a small syntax quirk: the new /login route was accidentally placed after the if __name__ == "__main__": block. In Python, anything placed after if __name__ == "__main__": app.run(debug=True) won't be registered properly by Flask when the application starts up!

Let's fix that order so your login route is positioned correctly right above the if __name__ == "__main__": block.

Here is how the exact bottom of your app.py should look:

Python
@app.route("/clear_prompt")
def clear_prompt():
    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/execute_clear", methods=["POST"])
def execute_clear():
    choice = request.form.get("clear_budgets")
    database.clear_expenses()
    if choice == "yes":
        database.clear_budgets()
    return redirect(url_for("expenses_page"))

@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        name = request.form.get("user_name")
        if name:
            session['user_name'] = name.title()
        return redirect(url_for('home'))
    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

if __name__ == "__main__":
    app.run(debug=True)
Just move that if __name__ == "__main__": block down to the very bottom, save your app.py, and you are completely ready to push everything to GitHub and test your live app!

ready

Awesome! Let's get these final changes pushed live to Render so everything is fully updated and working.

Open your VS Code terminal and run these quick commands:

Bash
git add -A
git commit -m "Fix app.py route order for user login and finalize setup"
git push origin main
Once Render finishes its automatic build (takes about a minute), visit your live site to test it out:

Regular Visitors: Can go to /login, enter their name, and see their personalized "Hello, [Their Name]" greeting badge in the sidebar sidebar.

Blog Access: The blog page (/blog) is clean, read-only, and displays articles without any writing forms or edit buttons.

Owner Access: Your secret admin route (/admin/login) lets you securely log in with your password to manage and publish blog posts.

Let me know how it looks once it's live!

whats my admin passcode

Your admin passcode is mysecretpassword.

You can use it whenever you visit your /admin/login route to sign in as the owner and manage your blog posts!

does this mean that if someone else enters an expenses inside their site, it reflects on mine? because i am using on phone and its saving same thing on my laptop

No, not at all! That is not how your database works.

If you see the exact same expenses on both your phone and your laptop right now, it is simply because both devices are currently logged into the exact same web address (your Render URL) and pointing to the same online database hosted on Render.

Here is how it actually works behind the scenes:

If a stranger or a friend visits your site: They will see the app, they can type their name to get a personal greeting, and they can add expenses or savings goals. However, because SQLite runs locally on your Render web server as a single shared file for that deployment, any standard user entering data right now writes to that same backend database file unless user accounts are separated.

Why it matches your phone and laptop: You are viewing your own deployed app instance from two different screens.

If you want other users to have completely private, separate expense trackers so their numbers never mix with yours, each user would typically need their own user ID tied to their specific session in the database table—right now, your app saves all expenses into one central database table for the whole app.

Would you like to update your database queries so that each user only sees their own added expenses based on their session name?

yes naaaa

That is a very important catch! Right now, because your app uses a single shared SQLite database file on Render (spendwise.db), anyone visiting your live link is technically adding items to the exact same shared workspace—which is why your phone and laptop mirror each other.

If you want the app to be truly multi-user where everyone has their own private expenses and budgets based on the name they entered at login, we need to link the database tables to the user's name (session['user_name']).

Here is how we can isolate everyone's data so nobody else sees your numbers, and your phone and laptop stay completely separate unless you log in as the same person:

Step 1: Update your Database Functions (database.py)
We need to make sure every function that adds or fetches expenses, budgets, and savings goals filters them by the specific username.

Open your database file (wherever your database helper functions are defined, like database.py) and update your queries to include username:

Python
# Example for adding an expense with a username
def add_expense(username, title, amount, category, date):
    conn = sqlite3.connect('spendwise.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (username, title, amount, category, date) VALUES (?, ?, ?, ?, ?)", 
                   (username, title, amount, category, date))
    conn.commit()
    conn.close()

# Example for getting expenses only for the logged-in user
def get_expenses(username):
    conn = sqlite3.connect('spendwise.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category, date FROM expenses WHERE username = ?", (username,))
    expenses = cursor.fetchall()
    conn.close()
    return expenses
Step 2: Pass the Username in app.py
In your app.py, whenever you call a database function, pass session.get('user_name') so it only pulls data belonging to whoever is currently logged in:

Python
@app.route("/dashboard")
def index():
    current_user = session.get('user_name', 'Friend')
    expenses = database.get_expenses(current_user)
    total = database.get_total_spending(current_user)
    # ... rest of your code
Would you like to look at your database.py file together so we can quickly update the table columns to separate everyone's data?

done

That is amazing!

Now that your app supports user sessions, personalized greetings, and secure admin blog management, your multi-user architecture is coming together brilliantly.

Whenever you're ready to look at updating your database file (database.py) to fully isolate each user's expenses and budgets by their name, just let me know and we can map it out step by step!

ready

Awesome! Since you're ready, let's make sure your database functions in database.py are fully updated to handle user-specific data so that every person logged into your app has their own private workspace.

Let's check your database.py file. Could you share what your current database functions look like (especially how tables are created and how expenses/budgets are saved and fetched)? That way, we can quickly add the username column to your SQLite tables and keep your personal data completely separate from anyone else using your live link!

import sqlite3



def init_db():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

   

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS expenses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            amount REAL NOT NULL,

            category TEXT NOT NULL,

            date TEXT NOT NULL

        )

    """)

   

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS budgets (

            category TEXT PRIMARY KEY,

            limit_amount REAL NOT NULL

        )

    """)

   

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS savings_goals (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL,

            target_amount REAL NOT NULL,

            current_amount REAL DEFAULT 0.0

        )

    """)

   

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS blog_posts (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL,

            content TEXT NOT NULL,

            image_url TEXT,

            date TEXT NOT NULL

        )

    """)

   

    conn.commit()

    conn.close()



def add_expense(title, amount, category, date):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (title, amount, category, date) VALUES (?, ?, ?, ?)",

                   (title, amount, category, date))

    conn.commit()

    conn.close()



def get_expenses():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")

    rows = cursor.fetchall()

    conn.close()

    return rows



def delete_expense(expense_id):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()

    conn.close()



def clear_expenses():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses")

    cursor.execute("DELETE FROM sqlite_sequence WHERE name='expenses'")

    conn.commit()

    conn.close()



def clear_budgets():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM budgets")

    conn.commit()

    conn.close()



def delete_budget(category):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM budgets WHERE category = ?", (category,))

    conn.commit()

    conn.close()



def get_total_spending():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")

    total = cursor.fetchone()[0]

    conn.close()

    return total if total is not None else 0.0



def set_budget(category, limit_amount):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO budgets (category, limit_amount)

        VALUES (?, ?)

        ON CONFLICT(category) DO UPDATE SET limit_amount = ?

    """, (category.title(), limit_amount, limit_amount))

    conn.commit()

    conn.close()



def get_budgets():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM budgets")

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_category_spending(category):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ?", (category,))

    total = cursor.fetchone()[0]

    conn.close()

    return total if total is not None else 0.0



def add_savings_goal(name, target_amount, current_amount):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO savings_goals (name, target_amount, current_amount) VALUES (?, ?, ?)",

                   (name.title(), target_amount, current_amount))

    conn.commit()

    conn.close()



def get_savings_goals():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM savings_goals")

    rows = cursor.fetchall()

    conn.close()

    return rows



def delete_savings_goal(goal_id):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM savings_goals WHERE id = ?", (goal_id,))

    conn.commit()

    conn.close()



def get_daily_summary():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT date, SUM(amount), COUNT(*)

        FROM expenses

        GROUP BY date

        ORDER BY date DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows



def get_monthly_summary():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("""

        SELECT strftime('%Y-%m', date) as month, SUM(amount), COUNT(*)

        FROM expenses

        GROUP BY month

        ORDER BY month DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    return rows



def add_blog_post(title, content, image_url, date):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("INSERT INTO blog_posts (title, content, image_url, date) VALUES (?, ?, ?, ?)",

                   (title, content, image_url, date))

    conn.commit()

    conn.close()



def get_blog_posts():

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM blog_posts ORDER BY id DESC")

    rows = cursor.fetchall()

    conn.close()

    return rows



def delete_blog_post(post_id):

    conn = sqlite3.connect("expenses.db")

    cursor = conn.cursor()

    cursor.execute("DELETE FROM blog_posts WHERE id = ?", (post_id,))

    conn.commit()

    conn.close()



# Example for adding an expense with a username

def add_expense(username, title, amount, category, date):

    conn = sqlite3.connect('spendwise.db')

    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (username, title, amount, category, date) VALUES (?, ?, ?, ?, ?)",

                   (username, title, amount, category, date))

    conn.commit()

    conn.close()



# Example for getting expenses only for the logged-in user

def get_expenses(username):

    conn = sqlite3.connect('spendwise.db')

    cursor = conn.cursor()

    cursor.execute("SELECT id, title, amount, category, date FROM expenses WHERE username = ?", (username,))

    expenses = cursor.fetchall()

    conn.close()

    return expenses

To fully isolate user data, we need to do two things with this file:

Add a username column to the expenses, budgets, and savings_goals tables so each person's data is stored with their name.

Update all database functions to accept and filter by username (while keeping blog posts global since only you manage them as admin).

Here is your complete, updated database.py file. You can copy and replace your entire database.py file with this:

Python
import sqlite3

def init_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            title TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            category TEXT NOT NULL,
            limit_amount REAL NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS savings_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            name TEXT NOT NULL,
            target_amount REAL NOT NULL,
            current_amount REAL DEFAULT 0.0
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blog_posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            image_url TEXT,
            date TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def add_expense(username, title, amount, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (username, title, amount, category, date) VALUES (?, ?, ?, ?, ?)", 
                   (username, title, amount, category, date))
    conn.commit()
    conn.close()

def get_expenses(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, amount, category, date FROM expenses WHERE username = ? ORDER BY date DESC", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE id = ? AND username = ?", (expense_id, username))
    conn.commit()
    conn.close()

def clear_expenses(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM expenses WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def clear_budgets(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def delete_budget(category, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM budgets WHERE category = ? AND username = ?", (category, username))
    conn.commit()
    conn.close()

def get_total_spending(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE username = ?", (username,))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def set_budget(username, category, limit_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    # Check if budget already exists for this user and category
    cursor.execute("SELECT id FROM budgets WHERE username = ? AND category = ?", (username, category.title()))
    row = cursor.fetchone()
    if row:
        cursor.execute("UPDATE budgets SET limit_amount = ? WHERE username = ? AND category = ?", (limit_amount, username, category.title()))
    else:
        cursor.execute("INSERT INTO budgets (username, category, limit_amount) VALUES (?, ?, ?)", (username, category.title(), limit_amount))
    conn.commit()
    conn.close()

def get_budgets(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category, limit_amount FROM budgets WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_category_spending(category, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses WHERE category = ? AND username = ?", (category, username))
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0

def add_savings_goal(username, name, target_amount, current_amount):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO savings_goals (username, name, target_amount, current_amount) VALUES (?, ?, ?, ?)", 
                   (username, name.title(), target_amount, current_amount))
    conn.commit()
    conn.close()

def get_savings_goals(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, target_amount, current_amount FROM savings_goals WHERE username = ?", (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_savings_goal(goal_id, username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM savings_goals WHERE id = ? AND username = ?", (goal_id, username))
    conn.commit()
    conn.close()

def get_daily_summary(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT date, SUM(amount), COUNT(*) 
        FROM expenses 
        WHERE username = ?
        GROUP BY date 
        ORDER BY date DESC
    """, (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_monthly_summary(username):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT strftime('%Y-%m', date) as month, SUM(amount), COUNT(*) 
        FROM expenses 
        WHERE username = ?
        GROUP BY month 
        ORDER BY month DESC
    """, (username,))
    rows = cursor.fetchall()
    conn.close()
    return rows

# Blog functions remain global for the admin
def add_blog_post(title, content, image_url, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_posts (title, content, image_url, date) VALUES (?, ?, ?, ?)", 
                   (title, content, image_url, date))
    conn.commit()
    conn.close()

def get_blog_posts():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_posts ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_blog_post(post_id):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM blog_posts WHERE id = ?", (post_id,))
    conn.commit()
    conn.close()
Save this file, and next we'll make sure your app.py passes the logged-in username into these database functions!

done

Now that your database is fully ready to isolate every user's data by their username, the final step is to make sure your routes in app.py pass the current user's name (session.get('user_name', 'Friend')) into these database functions!

Whenever you're ready, share your current routes in app.py (like where you call database.add_expense(), database.get_expenses(), etc.), and we will update them together so that your phone, your laptop, and any other visitors all have completely private, independent expense trackers!

@app.before_request

def before_request():

    if 'currency' not in session:

        session['currency'] = '₦'

    if 'user_name' not in session:

        session['user_name'] = 'Friend'  # Default greeting for regular visitors



@app.route("/set_currency", methods=["POST"])

def set_currency():

    selected_currency = request.form.get("currency")

    if selected_currency in CURRENCIES:

        session['currency'] = selected_currency

    return redirect(request.referrer or url_for('home'))



# NOTE: The /set_name route was removed here so users cannot change names manually!



@app.route("/")

def home():

    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/dashboard")

def index():

    current_user = session.get('user_name', 'Friend')

    expenses = database.get_expenses(current_user)

    total = database.get_total_spending(current_user)

    expenses = database.get_expenses()

    total = database.get_total_spending()

    raw_budgets = database.get_budgets()

    goals = database.get_savings_goals()

   

    day_of_year = datetime.datetime.now().timetuple().tm_yday

    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]

   

    budgets = []

    for cat, limit in raw_budgets:

        spent = database.get_category_spending(cat)

        remaining = limit - spent

        percentage = (spent / limit * 100) if limit > 0 else 0

        budgets.append({

            "category": cat,

            "limit": limit,

            "spent": spent,

            "remaining": remaining,

            "percentage": round(percentage, 1)

        })

       

    return render_template("index.html", total=total, budgets=budgets, goals=goals, expenses=expenses[:5],

                           currency=session.get('currency', '₦'), currencies=CURRENCIES, daily_tip=daily_tip)



@app.route("/expenses")

def expenses_page():

    expenses = database.get_expenses()

    total = database.get_total_spending()

    return render_template("expenses.html", expenses=expenses, total=total,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/budgets")

def budgets_page():

    raw_budgets = database.get_budgets()

    budgets = []

    for cat, limit in raw_budgets:

        spent = database.get_category_spending(cat)

        remaining = limit - spent

        percentage = (spent / limit * 100) if limit > 0 else 0

        budgets.append({

            "category": cat,

            "limit": limit,

            "spent": spent,

            "remaining": remaining,

            "percentage": round(percentage, 1)

        })

    return render_template("budgets.html", budgets=budgets,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/savings")

def savings_page():

    goals = database.get_savings_goals()

    return render_template("savings.html", goals=goals,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/reports")

def reports_page():

    daily_summary = database.get_daily_summary()

    monthly_summary = database.get_monthly_summary()

    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary,

                           currency=session.get('currency', '₦'), currencies=CURRENCIES)



# --- SECURE BLOG & ADMIN ROUTES ---



@app.route("/blog")

def blog_page():

    posts = database.get_blog_posts()

    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/admin/login", methods=["GET", "POST"])

def admin_login():

    if request.method == "POST":

        passcode = request.form.get("passcode")

        if passcode == "mysecretpassword":  # You can change this password to anything you want!

            session['is_admin'] = True

            session['user_name'] = 'Ikeli'  # Automatically sets your owner name when you log in

            return redirect(url_for("admin_blog"))

        else:

            return render_template("admin_login.html", error="Incorrect Passcode", currency=session.get('currency', '₦'), currencies=CURRENCIES)

    return render_template("admin_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/admin/blog", methods=["GET", "POST"])

def admin_blog():

    if not session.get('is_admin'):

        return redirect(url_for("admin_login"))

       

    if request.method == "POST":

        title = request.form.get("title")

        content = request.form.get("content")

        image_url = request.form.get("image_url")

        date = request.form.get("date")

        database.add_blog_post(title, content, image_url, date)

        return redirect(url_for("blog_page"))

       

    posts = database.get_blog_posts()

    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/admin/blog/delete/<int:post_id>")

def delete_blog(post_id):

    if not session.get('is_admin'):

        return redirect(url_for("admin_login"))

    database.delete_blog_post(post_id)

    return redirect(url_for("admin_blog"))



# --- ALL OTHER APP ROUTES REMAIN THE SAME ---



@app.route("/add", methods=["POST"])

def add():

    title = request.form.get("title").title()

    amount = float(request.form.get("amount"))

    category = request.form.get("category").title()

    date = request.form.get("date")

    database.add_expense(title, amount, category, date)

    return redirect(url_for("expenses_page"))



@app.route("/set_budget", methods=["POST"])

def set_budget():

    category = request.form.get("category").title()

    limit_amount = float(request.form.get("limit_amount"))

    database.set_budget(category, limit_amount)

    return redirect(url_for("budgets_page"))



@app.route("/add_goal", methods=["POST"])

def add_goal():

    name = request.form.get("name").title()

    target_amount = float(request.form.get("target_amount"))

    current_amount = float(request.form.get("current_amount") or 0.0)

    database.add_savings_goal(name, target_amount, current_amount)

    return redirect(url_for("savings_page"))



@app.route("/delete/<int:expense_id>")

def delete(expense_id):

    database.delete_expense(expense_id)

    return redirect(url_for("expenses_page"))



@app.route("/delete_budget/<string:category>")

def delete_budget(category):

    database.delete_budget(category)

    return redirect(url_for("budgets_page"))



@app.route("/delete_goal/<int:goal_id>")

def delete_goal(goal_id):

    database.delete_savings_goal(goal_id)

    return redirect(url_for("savings_page"))



@app.route("/clear_prompt")

def clear_prompt():

    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



@app.route("/execute_clear", methods=["POST"])

def execute_clear():

    choice = request.form.get("clear_budgets")

    database.clear_expenses()

    if choice == "yes":

        database.clear_budgets()

    return redirect(url_for("expenses_page"))



@app.route("/login", methods=["GET", "POST"])

def user_login():

    if request.method == "POST":

        name = request.form.get("user_name")

        if name:

            session['user_name'] = name.title()

        return redirect(url_for('home'))

    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)



if __name__ == "__main__":

    app.run(debug=True)

Your app.py routes currently call the database functions without passing the user's name, which would cause an error now that the database requires a username parameter for isolation!

Here is your fully updated app.py file. It grabs current_user = session.get('user_name', 'Friend') in every route and passes it securely to your database functions so that each user's data remains completely private:

Python
import datetime
from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for session management

# Initialize database tables on startup
database.init_db()

# Currency dictionary for the dropdown
CURRENCIES = {
    '₦': 'Nigerian Naira (NGN)',
    '$': 'US Dollar (USD)',
    '€': 'Euro (EUR)',
    '£': 'British Pound (GBP)',
    'C$': 'Canadian Dollar (CAD)',
    'A$': 'Australian Dollar (AUD)',
    '¥': 'Japanese Yen (JPY)',
    '₹': 'Indian Rupee (INR)'
}

DAILY_TIPS = [
    "Pay yourself first: set aside savings before you start spending.",
    "Track every penny: awareness is the first step to financial control.",
    "Avoid impulse buying: wait 24 hours before making non-essential purchases.",
    "Review your subscriptions today—cancel what you no longer use.",
    "Build your emergency fund a little bit at a time; consistency is key.",
    "Small daily savings compound into massive freedom over time.",
    "Never rely on a single income stream; nurture a secondary skill or hustle.",
    "Distinguish clearly between your absolute needs and temporary wants.",
    "A budget doesn't restrict your freedom; it gives you clarity and control.",
    "Review your active category budgets today to stay well ahead of limits.",
    "Automate your savings so you never have to rely on willpower alone.",
    "High-interest debt is an emergency—tackle it aggressively.",
    "Invest in your own knowledge; financial literacy pays the best dividends.",
    "Audit your bank statements monthly to catch hidden fees or leaks.",
    "Always shop with a grocery list to prevent unnecessary cart additions.",
    "Live below your means today so you can live above them tomorrow.",
    "Define your financial goals clearly with specific timelines and amounts.",
    "Protect your income with adequate insurance coverage for peace of mind.",
    "Treat windfalls (bonuses, gifts) like savings opportunities, not spending sprees.",
    "Beware of lifestyle inflation as your income grows.",
    "Compound interest is the eighth wonder of the world—start early.",
    "Keep your fixed expenses as low as possible to maximize flexibility.",
    "Learn to say 'no' to social spending that doesn't align with your goals.",
    "Check your credit score regularly and maintain healthy credit habits.",
    "Compare prices online before making major appliance or tech purchases.",
    "Build a 3 to 6-month emergency cushion before jumping into riskier investments.",
    "Diversify your income streams to insulate yourself against economic shocks.",
    "Negotiate your bills and subscription rates annually.",
    "Remember that time in the market beats timing the market.",
    "Avoid buying things you don't need with money you don't have to impress people you don't like.",
    "Set up a sinking fund for predictable annual expenses like insurance or holidays.",
    "Keep your investment strategy simple, consistent, and long-term.",
    "Rebalance your portfolio or savings allocations at least once a year.",
    "Make saving a habit rather than an afterthought.",
    "Patience is your greatest asset when building long-term wealth.",
    "Avoid retail therapy; find healthier, free ways to destress.",
    "Keep a dedicated folder or digital vault for all important financial documents.",
    "Understand the difference between good debt (assets) and bad debt (liabilities).",
    "Don't invest in anything you don't fully understand.",
    "Celebrate small financial milestones to stay motivated on your journey.",
    "Plan your meals weekly to dramatically cut down on restaurant and takeout spending.",
    "Pay off your credit card balance in full every single month to avoid interest.",
    "Build an attitude of gratitude; contentment reduces the urge to overspend.",
    "Review your utility usage and find ways to cut energy and water waste.",
    "Treat your future self as your most important dependent.",
    "Keep your financial goals private and your discipline public.",
    "Always read the fine print before signing any financial contract or loan.",
    "Establish a monthly money date with yourself to review your ledger.",
    "Prioritize experiences over accumulating clutter.",
    "Learn basic cooking skills; eating out is one of the biggest wealth drains.",
    "Don't let emotions dictate your investment or spending decisions.",
    "Create a buffer in your checking account to avoid accidental overdraft fees.",
    "Give generously when you can, but never at the expense of your own stability.",
    "Take advantage of employer-matching retirement programs if available.",
    "Keep track of your net worth quarterly to watch your progress compound.",
    "Buy quality items that last longer rather than cheap items you must replace often.",
    "Always get a second opinion or quote before undertaking major repairs.",
    "Maintain a zero-based budget mindset: every unit of currency has a job.",
    "Avoid checking your investment balances every day to prevent emotional panic.",
    "Understand your risk tolerance before committing funds to volatile assets.",
    "Keep your emergency fund in a liquid, easily accessible high-yield account.",
    "Set clear boundaries with family and friends regarding lending money.",
    "Master the art of delayed gratification; it is the cornerstone of wealth.",
    "Learn to negotiate prices, whether buying a car or contracting a service.",
    "Cut your commute costs by carpooling, biking, or utilizing public transit when possible.",
    "Never invest money you cannot afford to lose or tie up long-term.",
    "Keep your passwords, financial logins, and backups ultra-secure.",
    "Read at least one foundational book on personal finance every year.",
    "Avoid lifestyle comparisons on social media; most of it is curated illusion.",
    "Use cash or debit instead of credit if you struggle with impulse spending.",
    "Check your tax deductions and credits to ensure you aren't overpaying.",
    "Build a resilient mindset that views financial setbacks as learning curves.",
    "Establish a sinking fund for vehicle maintenance and unexpected repairs.",
    "Keep your goals visible—print them out or set them as your wallpaper.",
    "Remember that financial freedom gives you the power to choose your path.",
    "Take time to understand inflation and how it impacts your purchasing power.",
    "Always maintain a healthy separation between your personal and business funds.",
    "Avoid co-signing loans unless you are fully prepared to pay them off yourself.",
    "Focus on increasing your earning potential through continuous skill acquisition.",
    "Keep your home energy-efficient to shave down monthly utility bills.",
    "Practice mindful spending: ask 'Does this add genuine value to my life?'",
    "Establish clear financial roles and open communication if you share finances.",
    "Avoid keeping large sums of cash sitting idle in low-yield checking accounts.",
    "Schedule periodic financial decluttering sessions to review assets and debts.",
    "Embrace frugality as a tool for freedom, not as a punishment.",
    "Don't try to time the economy; focus on your personal savings rate instead.",
    "Protect your physical and mental health—medical bills are a primary cause of debt.",
    "Keep your financial records organized so tax season is stress-free.",
    "Learn how compounding works against you when paying high interest rates.",
    "Build relationships with mentors who have achieved financial wisdom.",
    "Turn off shopping app notifications to reduce subconscious temptation.",
    "Invest in tools and software that save you time and protect your data.",
    "Reevaluate your insurance policies every few years to find better rates.",
    "Keep your financial vision anchored on long-term peace of mind.",
    "Celebrate progress, not perfection; every step forward counts.",
    "Understand your spending triggers and build healthy coping mechanisms.",
    "Protect your digital identity against phishing and financial fraud.",
    "Make peace with your financial past and focus entirely on your future.",
    "Commit to continuous financial learning; the economic landscape always evolves.",
    "Your wealth is measured by the peace of mind it buys, not just the numbers.",
    # Days 101 - 200
    "Review your insurance deductibles to find the sweet spot for your risk profile.",
    "Avoid holding excessive cash beyond your emergency fund; let idle money work.",
    "Separate your needs, wants, and savings into distinct mental or physical accounts.",
    "Schedule an annual review for all your monthly service providers and utilities.",
    "Learn the basics of tax-advantaged accounts available in your region.",
    "Practice the '30-day rule' for major non-essential purchases.",
    "Keep your emergency fund untouched except for genuine, unforeseen crises.",
    "Treat your career like a business; constantly upgrade your marketable skills.",
    "Understand that financial discipline is a muscle that strengthens with use.",
    "Avoid buying brand-new items when high-quality secondhand options exist.",
    "Maintain a clear record of all digital subscriptions and auto-renewals.",
    "Focus on reducing your cost of living before seeking complex investment vehicles.",
    "Cultivate patience; wealth accumulation is a marathon, not a sprint.",
    "Never underestimate the power of a small, consistent monthly contribution.",
    "Keep your financial aspirations aligned with your core personal values.",
    "Review your bank's fee schedule to ensure you aren't leaking money needlessly.",
    "Build a network of supportive peers who value financial growth and education.",
    "Set up automated notifications for low account balances to avoid overdrafts.",
    "Recognize that saying no to unnecessary expenses is saying yes to your future.",
    "Keep your debt-to-income ratio as low as possible for financial flexibility.",
    "Learn to differentiate between asset classes: stocks, real estate, cash, and bonds.",
    "Revisit your budget monthly to adjust for changing seasonal expenses.",
    "Avoid emotional spending triggered by stress, fatigue, or boredom.",
    "Ensure your beneficiaries and estate documents are updated regularly.",
    "Take full advantage of free educational resources and financial libraries.",
    "Keep your financial goals realistic yet challenging enough to inspire growth.",
    "Prioritize paying off high-fee consumer loans over low-interest obligations.",
    "Practice mindful grocery shopping to minimize food waste and save cash.",
    "Keep a running log of your monthly financial wins, no matter how small.",
    "Understand how currency fluctuations can impact your savings and purchasing power.",
    "Build a robust password management routine to safeguard your financial portals.",
    "Avoid chasing speculative trends or 'get rich quick' investment schemes.",
    "Embrace minimalist principles to reduce clutter and curb impulse buying.",
    "Verify that your emergency fund yield beats or matches baseline inflation.",
    "Schedule regular check-ins with your partner or family to discuss money goals.",
    "Keep your financial stress in check by focusing only on factors you can control.",
    "Invest in durable household goods that require fewer replacements over time.",
    "Learn the mechanics of compound inflation and how it erodes uninvested cash.",
    "Keep your financial records transparent and easily accessible for emergencies.",
    "Avoid upgrading your phone or tech gadgets until they stop serving your needs.",
    "Establish clear criteria before lending your time, money, or resources.",
    "Treat every dollar as an employee working hard for your future freedom.",
    "Review your investment fees annually; high expense ratios eat your returns.",
    "Build resilience by having multiple backup plans for your primary income.",
    "Keep your financial ledger up to date every single week without fail.",
    "Practice gratitude for what you have while striving for smart financial growth.",
    "Understand the tax implications of every investment vehicle you choose.",
    "Avoid keeping credit card details saved on retail websites to prevent impulse buys.",
    "Set aside time to study global economic trends and historical market cycles.",
    "Keep your long-term vision clear even when short-term market volatility strikes.",
    "Prioritize your health today to prevent catastrophic medical expenses tomorrow.",
    "Learn to negotiate your starting salary and benefits package professionally.",
    "Keep your fixed monthly overhead minimal to weather unexpected income dips.",
    "Avoid letting lifestyle creep absorb every single raise or promotion you receive.",
    "Establish a dedicated savings goal for your next major life milestone.",
    "Check your bank statements for unauthorized or forgotten recurring charges.",
    "Build a habit of reading financial news and expert analysis weekly.",
    "Understand that true wealth is freedom of time and peace of mind.",
    "Keep your investment portfolio diversified across various sectors and industries.",
    "Avoid making major financial decisions when experiencing intense emotions.",
    "Set up clear savings milestones with visual trackers to stay motivated.",
    "Practice intentional gift-giving that values thoughtfulness over high price tags.",
    "Keep your financial independence as a top priority throughout all life stages.",
    "Learn how to read financial statements and corporate balance sheets.",
    "Avoid keeping all your eggs in one basket; diversification protects capital.",
    "Take time to appreciate free recreational activities like hiking and reading.",
    "Keep your debt payments automated to avoid late fees and credit penalties.",
    "Understand the psychological triggers that encourage you to spend money.",
    "Build a sustainable financial routine that requires minimal daily willpower.",
    "Review your utility and grocery bills quarterly to catch creeping inflation.",
    "Keep your financial documents backed up securely in a digital vault.",
    "Avoid comparing your chapter one to someone else's chapter twenty.",
    "Prioritize paying down principal balances on loans whenever extra cash arrives.",
    "Learn the importance of asset allocation tailored to your specific age and goals.",
    "Keep your spending aligned with your deepest personal convictions.",
    "Avoid impulse purchases by walking away from the item for 48 hours.",
    "Establish a clear emergency communication plan for family financial crises.",
    "Understand how interest rates set by central banks affect your borrowing costs.",
    "Keep your investment strategy boring, disciplined, and consistent.",
    "Embrace the power of compounding by starting your savings journey today.",
    "Review your monthly subscriptions and eliminate any duplicate streaming services.",
    "Build a buffer in your savings account specifically for holiday and gift expenses.",
    "Keep your financial goals flexible enough to adapt to major life transitions.",
    "Avoid taking on debt to finance depreciating consumer assets.",
    "Prioritize building a strong credit history early in your adult life.",
    "Learn how to audit your monthly cash flow to find hidden savings opportunities.",
    "Keep your investment horizon long-term to ride out short-term market turbulence.",
    "Practice mindful consumption by repairing items instead of replacing them instantly.",
    "Establish clear financial boundaries when navigating social and family events.",
    "Understand the true cost of convenience spending versus cooking at home.",
    "Keep your focus on net worth growth rather than gross income display.",
    "Avoid letting fear paralyze you from making smart, calculated financial moves.",
    "Set up automatic alerts for any unusual activity on your financial accounts.",
    "Embrace the discipline of living below your means as a badge of honor.",
    "Review your professional skills and identify areas for high-ROI improvement.",
    "Keep your financial philosophy grounded in simplicity, patience, and consistency.",
    "Remember that every financial choice you make today shapes your tomorrow.",
    # Days 201 - 365
    "Master the art of cost-per-use calculation before buying expensive items.",
    "Keep your investment thesis simple: buy quality assets and hold them patiently.",
    "Avoid carrying balances on multiple credit cards simultaneously.",
    "Establish a routine for backing up all your digital financial records.",
    "Understand how fiscal policy and taxation influence your take-home pay.",
    "Keep your financial education ongoing through podcasts, books, and articles.",
    "Practice delayed gratification as a core philosophy in every area of life.",
    "Review your insurance policies annually to ensure adequate coverage limits.",
    "Avoid participating in crowd mentality or hype-driven financial bubbles.",
    "Build a contingency fund specifically for freelance or variable income drops.",
    "Keep your physical wallet lean by removing unused store credit cards.",
    "Understand the long-term cost of borrowing money for non-essential luxuries.",
    "Embrace frugality not as deprivation, but as targeted resource allocation.",
    "Review your investment portfolio risk exposure as you approach major milestones.",
    "Avoid co-signing loans unless you have fully accepted the risk of repayment.",
    "Establish a monthly ritual to celebrate your progress toward debt freedom.",
    "Keep your fixed expenses below 50% of your net take-home income.",
    "Learn how to evaluate corporate earnings reports and fundamental data.",
    "Avoid impulse buying online by clearing your saved payment card details.",
    "Build a strong relationship with your bank or credit union advisors.",
    "Keep your financial targets visible in your workspace as daily motivators.",
    "Understand the mechanics of inflation-protected securities and savings bonds.",
    "Practice gratitude daily; appreciation for what you have reduces spending urges.",
    "Review your career trajectory and negotiate compensation packages proactively.",
    "Avoid letting temporary market downturns derail your long-term strategy.",
    "Establish a dedicated savings allocation for continuous personal development.",
    "Keep your home maintenance proactive to avoid costly emergency repairs later.",
    "Understand the difference between being rich and building genuine wealth.",
    "Embrace the discipline of tracking every single transaction without exception.",
    "Review your utility providers annually to switch to more affordable tariffs.",
    "Avoid buying extended warranties on consumer electronics and appliances.",
    "Build an emergency plan for your digital assets and online accounts.",
    "Keep your financial expectations realistic and grounded in mathematical reality.",
    "Learn the value of networking with financially literate mentors and peers.",
    "Avoid making snap decisions on major purchases during holiday sales.",
    "Establish a clear succession plan and will for your estate and assets.",
    "Keep your investment approach disciplined, ignoring daily media noise.",
    "Understand how psychological accounting influences your spending habits.",
    "Practice mindful energy consumption to lower monthly utility overhead.",
    "Review your subscription list every ninety days without fail.",
    "Avoid funding your lifestyle with short-term payday loans or high-interest cash advances.",
    "Build a resilient mindset that views economic shifts as strategic opportunities.",
    "Keep your financial boundaries firm when dealing with high-pressure sales pitches.",
    "Learn the basics of estate planning and asset protection strategies.",
    "Avoid comparing your financial portfolio to unrealistic online benchmarks.",
    "Establish a sinking fund for annual travel and holiday vacations.",
    "Keep your savings automated so wealth building happens effortlessly in the background.",
    "Understand how compound interest accelerates your progress over decades.",
    "Embrace patience as your greatest ally in building generational stability.",
    "Review your credit report annually for errors and unauthorized inquiries.",
    "Avoid lifestyle inflation by saving 100% of every salary increase you receive.",
    "Build a comprehensive household inventory for insurance and security purposes.",
    "Keep your financial vision focused on long-term independence rather than status.",
    "Learn how to analyze risk-adjusted returns before entering new asset classes.",
    "Avoid letting greed cloud your judgment when evaluating investment opportunities.",
    "Establish a monthly habit of reviewing your net worth statement.",
    "Keep your fixed overhead minimal to maintain maximum personal freedom.",
    "Understand the importance of liquidity when structuring your financial portfolio.",
    "Practice intentional spending that aligns directly with your personal values.",
    "Review your tax withholding strategy annually with a qualified professional.",
    "Avoid keeping large balances in accounts that offer negligible interest rates.",
    "Build a habit of negotiating service fees, insurance rates, and contract prices.",
    "Keep your financial passwords secure and update your security protocols regularly.",
    "Understand the psychological impact of advertising and resist its subtle pulls.",
    "Embrace the discipline of living below your means as the ultimate superpower.",
    "Review your financial goals at the start of every new quarter.",
    "Avoid investing in complex financial products you cannot explain simply.",
    "Build a strong foundation of emergency savings before exploring riskier ventures.",
    "Keep your focus fixed on steady, predictable progress rather than overnight riches.",
    "Learn how to calculate your true hourly wage after factoring in commute costs.",
    "Avoid emotional attachments to declining assets or unprofitable investments.",
    "Establish clear financial milestones for every stage of your adult life.",
    "Keep your personal financial data completely confidential and secure.",
    "Understand the power of saying no to social pressure and lifestyle traps.",
    "Embrace continuous learning as the cornerstone of lifelong financial security.",
    "Review your banking and brokerage statements line by line every month.",
    "Avoid letting short-term financial setbacks distract you from your long-term vision.",
    "Build an attitude of abundance through gratitude, mindfulness, and smart planning.",
    "Keep your financial house in order so you can seize opportunities when they arise.",
    "Remember that true financial mastery is built one disciplined choice at a time."
]

@app.before_request
def before_request():
    if 'currency' not in session:
        session['currency'] = '₦'
    if 'user_name' not in session:
        session['user_name'] = 'Friend'  # Default greeting for regular visitors

@app.route("/set_currency", methods=["POST"])
def set_currency():
    selected_currency = request.form.get("currency")
    if selected_currency in CURRENCIES:
        session['currency'] = selected_currency
    return redirect(request.referrer or url_for('home'))

@app.route("/")
def home():
    return render_template("home.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/dashboard")
def index():
    current_user = session.get('user_name', 'Friend')
    expenses = database.get_expenses(current_user)
    total = database.get_total_spending(current_user)
    raw_budgets = database.get_budgets(current_user)
    goals = database.get_savings_goals(current_user)
    
    day_of_year = datetime.datetime.now().timetuple().tm_yday
    daily_tip = DAILY_TIPS[(day_of_year - 1) % len(DAILY_TIPS)]
    
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat, current_user)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
        
    return render_template("index.html", total=total, budgets=budgets, goals=goals, expenses=expenses[:5], 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES, daily_tip=daily_tip)

@app.route("/expenses")
def expenses_page():
    current_user = session.get('user_name', 'Friend')
    expenses = database.get_expenses(current_user)
    total = database.get_total_spending(current_user)
    return render_template("expenses.html", expenses=expenses, total=total, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/budgets")
def budgets_page():
    current_user = session.get('user_name', 'Friend')
    raw_budgets = database.get_budgets(current_user)
    budgets = []
    for cat, limit in raw_budgets:
        spent = database.get_category_spending(cat, current_user)
        remaining = limit - spent
        percentage = (spent / limit * 100) if limit > 0 else 0
        budgets.append({
            "category": cat,
            "limit": limit,
            "spent": spent,
            "remaining": remaining,
            "percentage": round(percentage, 1)
        })
    return render_template("budgets.html", budgets=budgets, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/savings")
def savings_page():
    current_user = session.get('user_name', 'Friend')
    goals = database.get_savings_goals(current_user)
    return render_template("savings.html", goals=goals, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/reports")
def reports_page():
    current_user = session.get('user_name', 'Friend')
    daily_summary = database.get_daily_summary(current_user)
    monthly_summary = database.get_monthly_summary(current_user)
    return render_template("reports.html", daily=daily_summary, monthly=monthly_summary, 
                           currency=session.get('currency', '₦'), currencies=CURRENCIES)

# --- SECURE BLOG & ADMIN ROUTES ---

@app.route("/blog")
def blog_page():
    posts = database.get_blog_posts()
    return render_template("blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        passcode = request.form.get("passcode")
        if passcode == "mysecretpassword":  # Owner passcode
            session['is_admin'] = True
            session['user_name'] = 'Ikeli'  # Automatically sets your owner name when you log in
            return redirect(url_for("admin_blog"))
        else:
            return render_template("admin_login.html", error="Incorrect Passcode", currency=session.get('currency', '₦'), currencies=CURRENCIES)
    return render_template("admin_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog", methods=["GET", "POST"])
def admin_blog():
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
        
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        image_url = request.form.get("image_url")
        date = request.form.get("date")
        database.add_blog_post(title, content, image_url, date)
        return redirect(url_for("blog_page"))
        
    posts = database.get_blog_posts()
    return render_template("admin_blog.html", posts=posts, currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/admin/blog/delete/<int:post_id>")
def delete_blog(post_id):
    if not session.get('is_admin'):
        return redirect(url_for("admin_login"))
    database.delete_blog_post(post_id)
    return redirect(url_for("admin_blog"))

# --- USER DATA ACTION ROUTES ---

@app.route("/add", methods=["POST"])
def add():
    current_user = session.get('user_name', 'Friend')
    title = request.form.get("title").title()
    amount = float(request.form.get("amount"))
    category = request.form.get("category").title()
    date = request.form.get("date")
    database.add_expense(current_user, title, amount, category, date)
    return redirect(url_for("expenses_page"))

@app.route("/set_budget", methods=["POST"])
def set_budget():
    current_user = session.get('user_name', 'Friend')
    category = request.form.get("category").title()
    limit_amount = float(request.form.get("limit_amount"))
    database.set_budget(current_user, category, limit_amount)
    return redirect(url_for("budgets_page"))

@app.route("/add_goal", methods=["POST"])
def add_goal():
    current_user = session.get('user_name', 'Friend')
    name = request.form.get("name").title()
    target_amount = float(request.form.get("target_amount"))
    current_amount = float(request.form.get("current_amount") or 0.0)
    database.add_savings_goal(current_user, name, target_amount, current_amount)
    return redirect(url_for("savings_page"))

@app.route("/delete/<int:expense_id>")
def delete(expense_id):
    current_user = session.get('user_name', 'Friend')
    database.delete_expense(expense_id, current_user)
    return redirect(url_for("expenses_page"))

@app.route("/delete_budget/<string:category>")
def delete_budget(category):
    current_user = session.get('user_name', 'Friend')
    database.delete_budget(category, current_user)
    return redirect(url_for("budgets_page"))

@app.route("/delete_goal/<int:goal_id>")
def delete_goal(goal_id):
    current_user = session.get('user_name', 'Friend')
    database.delete_savings_goal(goal_id, current_user)
    return redirect(url_for("savings_page"))

@app.route("/clear_prompt")
def clear_prompt():
    return render_template("clear_prompt.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

@app.route("/execute_clear", methods=["POST"])
def execute_clear():
    current_user = session.get('user_name', 'Friend')
    choice = request.form.get("clear_budgets")
    database.clear_expenses(current_user)
    if choice == "yes":
        database.clear_budgets(current_user)
    return redirect(url_for("expenses_page"))

@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "POST":
        name = request.form.get("user_name")
        if name:
            session['user_name'] = name.title()
        return redirect(url_for('home'))
    return render_template("user_login.html", currency=session.get('currency', '₦'), currencies=CURRENCIES)

if __name__ == "__main__":
    app.run(debug=True)