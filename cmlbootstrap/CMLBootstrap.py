import requests
import json
import logging
import os
import xml.etree.ElementTree as ET
import requests 
from requests_kerberos import HTTPKerberosAuth
import boto3


class CMLBootstrap:
    """Wrapper class for calls to the internal CML api.

    Attributes:
        host (str): URL for the CML instance host.
        username (str): Current username.
        api_key (str): API key.
        project_name (str): Project name.
    """

    def __init__(
            self, 
            host = os.getenv("CDSW_API_URL").split(":")[0] + "://" + os.getenv("CDSW_DOMAIN"), 
            username = os.getenv("HADOOP_USER_NAME"), 
            api_key= os.getenv("CDSW_API_KEY"), 
            project_name = os.getenv("CDSW_PROJECT"), 
            log_level=logging.INFO
        ):
        self.host = host
        self.username = username
        self.api_key = api_key
        self.project_name = project_name
        logging.basicConfig(level=log_level)

        logging.debug("Api Initiated")

    def get_default_engine(self, params={}):
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

    def get_user(self, params={}):
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

    def get_project(self, params={}):
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

    def get_jobs(self, params={}):
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

    def delete_job(self, job_id, params={}):
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

    def start_job(self, job_id, params={}):
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

    def stop_job(self, job_id, params={}):
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
            If you are looking for the models in the current project, use
            {"projectId" : project_id } as the params where project_id is an int of the project number.

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
        """Get model info given its id

        Arguments:
            params {dict} -- {id: modelId}

        Returns:
            dict -- [dictionary of model details].
        """        
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
        """Create a model

        Arguments:
            params {dict} -- [dictionary containing model parameters]

        Returns:
            [dict] -- [dictionary containing model details]
        """
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

    def rebuild_model(self, params):
        """Deploy a new model build

        Arguments:
            params {dict} -- [dictionary containing model parameters]

        Returns:
            [dict] -- [dictionary containing model details]
        """
        build_model_endpoint = "/".join([self.host,
                                          "api/altus-ds-1", "models", "build-model"])
        res = requests.post(
            build_model_endpoint,
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

    def set_model_auth(self, params):
        """Enable or disable Model Authentication

        Arguments:
            params {dict} -- None, example input {"id": 5, "enableAuth": False}
            app_id {str} -- id for appliacation to be retrieved

        Returns:
                    [dict] -- Nothing
        """
        set_model_auth_endpoint = "/".join([self.host,
                                            "api/altus-ds-1", "models", "set-model-auth"])
        res = requests.post(
            set_model_auth_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )
        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug(">> Set Model Auth")
        return response

    def get_application(self, app_id, params):
        """Get details for an application

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

    def get_applications(self, params={}):
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
        """Create an Application

        Arguments:
            params {dict} -- [dictionary containing application parameters]

        Returns:
            [dict] -- [dictionary containing job details]
        """
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

    def create_environment_variable(self, params):
        """Add project level environment variables

        Arguments:
            params {dict} -- [dictionary containing new environment variables]

        Returns:
            res.status_code
        """
        env_vars = self.get_environment_variables({})
        env_vars.update(params)

        create_environment_variable_endpoint = "/".join([self.host, "api/v1/projects",
                                                         self.username, self.project_name, "environment"])
        res = requests.put(
            create_environment_variable_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(env_vars)
        )
        #response = res.json()
        if (res.status_code != 204):
            logging.error("Reponse code was " + res.status_code)
        else:
            logging.debug("Environment variable created")

        return res.status_code

    def get_environment_variables(self, params={}):
        """Get the project level environment variables

        Arguments:
            params {dict} -- None needed.

        Returns:
            dict -- [dictionary containing project level environment variables]
        """
        create_environment_variable_endpoint = "/".join([self.host, "api/v1/projects",
                                                         self.username, self.project_name, "environment"])
    
        res = requests.get(
                create_environment_variable_endpoint,
                headers={"Content-Type": "application/json"},
                auth=(self.api_key, ""),
                data=json.dumps(params)
        )
        
        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Environment variables retrieved")

        return response
    
    def add_project_editor(self, params):
        add_project_editor_endpoint = "/".join([self.host, "api/v1/projects",
                                                         self.username, self.project_name, "editors"])
        res = requests.post(
            add_project_editor_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )
        response = res.json()
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Editor added")
        return response

    def get_cloud_storage(self):
        """Get the cloud storage URI

        Arguments:
            None.

        Returns:
            str -- The URI for the cloud storge location used for the default Data Lake Hive server
        """
        try:
            hadoop_conf_dir = os.environ['HADOOP_CONF_DIR']
            try:
                tree = ET.parse('{}/hive-site.xml'.format(hadoop_conf_dir))
                root = tree.getroot()
                for prop in root.findall('property'):
                    if prop.find('name').text == "hive.metastore.warehouse.dir":
                        storage = prop.find('value').text.split("/")[0] + "//" + prop.find('value').text.split("/")[2]
                logging.debug("Storage Variable Found")
            except:
                logging.error("hive-site.xml file not found")
        except:
            logging.error('HADOOP_CONF_DIR environment variable not defined')
        return storage
    
    def get_id_broker(self):
        """Get the ID Broker host name

        Arguments:
            None.

        Returns:
            str -- The hostname for the ID Broker for the default Data Lake
        """
        try:
            if os.path.exists('/etc/hadoop/conf/hive-site.xml'):
                hadoop_conf_dir = '/etc/hadoop/conf'
            else:
                hadoop_conf_dir = os.environ['HADOOP_CONF_DIR']
            try:
                tree = ET.parse('{}/core-site.xml'.format(hadoop_conf_dir))
                root = tree.getroot()
                for prop in root.findall('property'):
                    if prop.find('name').text == "fs.s3a.ext.cab.address":
                        id_broker = prop.find('value').text.split("//")[1].split(":")[0]
            except:
                logging.error("Unable to get S3 credentails")
        except:
            logging.error('HADOOP_CONF_DIR environment variable not defined')
        return id_broker


    def boto3_client(self,id_broker):
        """Retrieve S3 credentials from ID Broker and return a boto3 client.

        Arguments:
            None.

        Returns:
            boto3.client -- A boto3 client connected to the AWS environment
        """
        try:
            r = requests.get("https://{}:8444/gateway/dt/knoxtoken/api/v1/token".format(id_broker), auth=HTTPKerberosAuth())
            url = "https://{}:8444/gateway/aws-cab/cab/api/v1/credentials".format(id_broker)
            headers = {
                'Authorization': "Bearer "+ r.json()['access_token'],
                'cache-control': "no-cache"
                }

            response = requests.request("GET", url, headers=headers)
            ACCESS_KEY=response.json()['Credentials']['AccessKeyId']
            SECRET_KEY=response.json()['Credentials']['SecretAccessKey']
            SESSION_TOKEN=response.json()['Credentials']['SessionToken']
            client = boto3.client(
                's3',
                aws_access_key_id=ACCESS_KEY,
                aws_secret_access_key=SECRET_KEY,
                aws_session_token=SESSION_TOKEN,
            )
            logging.debug("S3 credential found and boto3 client instantiated")
        except:
            logging.error("Unable to get S3 credentails")
        return client
    
    def get_runtimes(self, params={}):
        """Get the list of runtimes including ids

        Arguments:
            params {dict} -- None needed.

        Returns:
            dict -- [dictionary containing runtimes and the associated details]
        """
        get_runtimes_endpoint = "/".join([self.host, "api/v1/runtimes?includeAll=true"])

        res = requests.get(
            get_runtimes_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )
        response = res.json()
        
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Runtime details retrieved")

        return response

    
    def get_runtimes_addons(self, params={"component":"Spark"}):
        """Get the list of runtime addons

        Arguments:
            params {dict} -- None needed.

        Returns:
            dict -- [dictionary containing runtime addons]
        """
        get_runtimes_endpoint = "/".join([self.host, "api/v1/runtime-addons"])

        res = requests.post(
            get_runtimes_endpoint,
            headers={"Content-Type": "application/json"},
            auth=(self.api_key, ""),
            data=json.dumps(params)
        )
        response = res.json()
        
        if (res.status_code != 200):
            logging.error(response["message"])
            logging.error(response)
        else:
            logging.debug("Runtime addon details retrieved")

        return response
    
