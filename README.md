# End-to-end machine learning project

Here, I follow [this tutotial](https://www.youtube.com/watch?v=Rv6UFGNmNZg) to build an end-to-end machine learning project

## my_notes:
### Setup GitHub repo:
1. Create a **repo** on Github & a local folder for the project on your local machine.
2. Activate **coda**: ```conda activate```
3. Open the project folder on the terminal/IDE terminal, and create a **virtual environment**, this will help separate the project dependencies from the system's and other projects' dependencies. ```conda create -p venv python==3.8 -y```
4. Activate the virtual environment ``` conda activate /venve```
5. Run ```git init``` to make this local folder a GitHub local repo. Its the very first command to run in any new project to enable gi commands.
6. **Connect** local and cloud repos:
   - The name of the main branch in your local repo is "master", while the main branch in the Github repo is "main", so Run ```git branch -M main``` to rename the "master" and be compatible with the default name of the cloud repo main branch.
   - Connect to the cloud by running: ```git remote add origin [link to the github repo]```
7. Create .gitignore:
   - On Github: add file
   - use python template
   - commit changes
   - on the local repo run:```git pull``` to update the local repo with the new changes
-----------------------------------------------------------------------------------
### File structure:
├── app.py   ((*Flak app for deployment*))<br />
├── templates<br />
│   ├── home.html<br />
│   └── index.html<br />
├── artefacts  ((*Contains data, trained models, transformers, etc...*))<br />
├── Dockerfile<br />
├── logs <br />
├── notebook<br />
├── README.md<br />
├── requirements.txt ((*```pip install requirements.txt``` to install dependencies*))<br />
├── setup.py ((*Defines the project name, author, version, etc..*))<br />
├── src<br />
│   ├── components<br />
│   │   ├── data_ingestion.py<br />
│   │   ├── data_transformation.py<br />
│   │   ├── __init__.py<br />
│   │   ├── model_training.py<br />
│   ├── exception.py<br />
│   ├── __init__.py<br />
│   ├── logger.py<br />
│   ├── pipeline<br />
│   └── utils.py ((*Reusable functions*))<br />
└── venv<br />
