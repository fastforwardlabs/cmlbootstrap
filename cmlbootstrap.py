import requests
import json
import logging


class CMLBootstrap:
    """wrapper for calls to the internal CML api

    Attributes:
        host (str): URL for the CML instance host.
        username (str): Current username.
        api_key (str): API key.
        project_name (str): Project name.
    """

    def __init__(self, host, username, api_key, project_name, log_level=logging.INFO):
        self.host = host
        self.username = username
        self.api_key = api_key
        self.project_name = project_name
        logging.basicConfig(level=log_level)

        logging.debug("Api Initiated")

    def get_default_engine(self, params):
        """Get the default engine for the given project

        Arguments:
            params {dict} -- None needed.

        Returns:
            dict -- [dictionary containing default engine details]
        """
        get_engines_endpoint = "/".join([self.host, "api/v1/projects",
                                         self.username, self.project_name, "engine-images"])

        res = requests.get(
            get_engines_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("User details retrieved")

        return response

    def get_user(self, params):
        """Get details for a given user

        Arguments:
            params {dict} -- [description]

        Returns:
            [dict] -- [dictionary containing user details]
        """

        get_user_endpoint = "/".join([self.host, "api/v1/users",
                                      self.username])
        res = requests.get(
            get_user_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("User details retrieved")

        return response

    def get_project(self, params):
        """Get details for a given project

        Arguments:
            params {dict} -- [project parameters]

        Returns:
            [dict] -- [dictionary containing project details]
        """
        get_project_endpoint = "/".join([self.host, "api/v1/projects",
                                         self.username, self.project_name])
        res = requests.get(
            get_project_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Project details retrieved")

        return response

    def run_experiment(self, params):
        """Run an experiment

        Arguments:
            params {dict} -- []

        Returns:
            [dict] -- []
        """
        run_experiment_endpoint = "/".join([self.host,
                                            "api/altus-ds-1", "ds", "run"])
        res = requests.post(
            run_experiment_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Experiment created")
        return response

    def get_jobs(self, params):
        """Return a list of jobs associated with the given project

        Arguments:
            params {dict} -- None

        Returns:
            list -- List of jobs
        """
        get_jobs_endpoint = "/".join([self.host, "api/v1/projects",
                                      self.username, self.project_name, "jobs"])
        res = requests.get(
            get_jobs_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("List of jobs retrieved")

        return response

    def delete_job(self, job_id, params):
        """Delete a job given its id

        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be deleted
        Returns:
            [dict] -- [None. delete endpoint does not return a value]
        """
        delete_job_endpoint = "/".join([self.host, "api/v1/projects",
                                        self.username, self.project_name, "jobs", str(job_id)])
        res = requests.delete(
            delete_job_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        if (res.status_code != 204):
            response = res.json()
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Job deleted")

        return None

    def create_job(self, params):
        """Create a job

        Arguments:
            params {dict} -- [description]

        Returns:
            [dict] -- [dictionary containing job details]
        """
        create_job_endpoint = "/".join([self.host, "api/v1/projects",
                                        self.username, self.project_name, "jobs"])
        res = requests.post(
            create_job_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 201):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Job created")
        return response

    def start_job(self, job_id, params):
        """Start a job    

        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be initalized

        Returns:
            [dict] -- [ ]
        """
        start_job_endpoint = "/".join([self.host, "api/v1/projects",
                                       self.username, self.project_name, "jobs", str(job_id), "start"])
        res = requests.post(
            start_job_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Job started")

        return response

    def stop_job(self, job_id, params):
        """Stop a job    

        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be stopped

        Returns:
            [dict] -- []
        """

        stop_job_endpoint = "/".join([self.host, "api/v1/projects",
                                      self.username, self.project_name, "jobs", str(job_id), "stop"])
        res = requests.post(
            stop_job_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        logging.error(response)
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Job stopped")

        return response

    def get_models(self, params):
        """Return a list of models associated with the given project

        Arguments:
            params {dict} -- None

        Returns:
            list -- List of models
        """
        get_models_endpoint = "/".join([self.host,
                                        "api/altus-ds-1", "models", "list-models"])
        res = requests.post(
            get_models_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("List of Models retrieved")

        return response

    def delete_model(self, params):
        """Delete a project given its id

        Arguments:
            params {dict} -- {id: projectId}

        Returns:
            dict -- Nothing.
        """
        delete_model_endpoint = "/".join([self.host,
                                          "api/altus-ds-1", "models", "delete-model"])
        res = requests.post(
            delete_model_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Model deleted")

        return response

    def get_model(self, params):
        get_model_endpoint = "/".join([self.host,
                                       "api/altus-ds-1", "models", "get-model"])
        res = requests.post(
            get_model_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(">> Got model")

        return response

    def create_model(self, params):
        create_model_endpoint = "/".join([self.host,
                                          "api/altus-ds-1", "models", "create-model"])
        res = requests.post(
            create_model_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Model created")

        return response

    def get_application(self, app_id, params):
        """Get details for an  application

        Arguments:
            params {dict} -- None
            app_id {str} -- id for appliacation to be retrieved

        Returns:
            {dict} -- dictionary of application details
        """
        get_application_endpoint = "/".join([self.host, "api/v1/projects",
                                             self.username, self.project_name, "applications", app_id])
        res = requests.get(
            get_application_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Application details retrieved")

        return response

    def get_applications(self, params):
        """Get list of applications within current project

        Arguments:
            params {dict} -- None

        Returns:
            list -- list of current applications
        """
        get_applications_endpoint = "/".join([self.host, "api/v1/projects",
                                              self.username, self.project_name, "applications"])
        res = requests.get(
            get_applications_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Application list retrieved")

        return response

    def delete_application(self, application_id, params):
        """Delete application given id

        Arguments:
            application_id {int} -- application id
            params {dict} -- application details

        Returns:
            None -- None
        """
        get_applications_endpoint = "/".join([self.host, "api/v1/projects",
                                              self.username, self.project_name, "applications", str(application_id)])
        res = requests.delete(
            get_applications_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        if (res.status_code != 200):
            response = res.json()
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Application deleted")

        return None

    def create_application(self, params):
        create_application_endpoint = "/".join([self.host, "api/v1/projects",
                                                self.username, self.project_name, "applications"])
        res = requests.post(
            create_application_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )

        response = res.json()
        if (res.status_code != 201):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(" Application created")

        return response
