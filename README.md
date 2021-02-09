# cs373-idb-gcp

This is an introductory tutorial shows how one can run a simple flask app with templates. It also deploys the app on GCP.

Do NOT forget to include:
- "venv" inside ".gitignore" to prevent pushing virtual environment to remote repo
- "requirements.txt"

By default, Flask dev server runs on localhost, i.e., 127.0.0.1, but you can change that
by speciftying "host='0.0.0.0'" within your "app.run()". In this case, the server will
run on your machine's IP address.


