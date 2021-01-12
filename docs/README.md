Module CMLBootstrap
===================

Classes
-------

`CMLBootstrap(host, username, api_key, project_name, log_level=20)`
:   Wrapper class for calls to the internal CML api.
    
    Attributes:
        host (str): URL for the CML instance host.
        username (str): Current username.
        api_key (str): API key.
        project_name (str): Project name.

    ### Methods

    `create_application(self, params)`
    :   Create an Application
        
        Arguments:
            params {dict} -- [dictionary containing application parameters]
        
        Returns:
            [dict] -- [dictionary containing job details]

    `create_job(self, params)`
    :   Create a job
        
        Arguments:
            params {dict} -- [description]
        
        Returns:
            [dict] -- [dictionary containing job details]

    `create_model(self, params)`
    :   Create a model
        
        Arguments:
            params {dict} -- [dictionary containing model parameters]
        
        Returns:
            [dict] -- [dictionary containing model details]

    `delete_application(self, application_id, params)`
    :   Delete application given id
        
        Arguments:
            application_id {int} -- application id
            params {dict} -- application details
        
        Returns:
            None -- None

    `delete_job(self, job_id, params)`
    :   Delete a job given its id
        
        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be deleted
        Returns:
            [dict] -- [None. delete endpoint does not return a value]

    `delete_model(self, params)`
    :   Delete a project given its id
        
        Arguments:
            params {dict} -- {id: projectId}
        
        Returns:
            dict -- Nothing.

    `get_application(self, app_id, params)`
    :   Get details for an application
        
        Arguments:
            params {dict} -- None
            app_id {str} -- id for appliacation to be retrieved
        
        Returns:
            {dict} -- dictionary of application details

    `get_applications(self, params)`
    :   Get list of applications within current project
        
        Arguments:
            params {dict} -- None
        
        Returns:
            list -- list of current applications

    `get_default_engine(self, params)`
    :   Get the default engine for the given project
        
        Arguments:
            params {dict} -- None needed.
        
        Returns:
            dict -- [dictionary containing default engine details]

    `get_jobs(self, params)`
    :   Return a list of jobs associated with the given project
        
        Arguments:
            params {dict} -- None
        
        Returns:
            list -- List of jobs

    `get_model(self, params)`
    :

    `get_models(self, params)`
    :   Return a list of models associated with the given project
        
        Arguments:
            params {dict} -- None
        
        Returns:
            list -- List of models

    `get_project(self, params)`
    :   Get details for a given project
        
        Arguments:
            params {dict} -- [project parameters]
        
        Returns:
            [dict] -- [dictionary containing project details]

    `get_user(self, params)`
    :   Get details for a given user
        
        Arguments:
            params {dict} -- [description]
        
        Returns:
            [dict] -- [dictionary containing user details]

    `run_experiment(self, params)`
    :   Run an experiment
        
        Arguments:
            params {dict} -- []
        
        Returns:
            [dict] -- []

    `start_job(self, job_id, params)`
    :   Start a job
        
        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be initalized
        
        Returns:
            [dict] -- [ ]

    `stop_job(self, job_id, params)`
    :   Stop a job
        
        Arguments:
            params {dict} -- [description]
            job_id {str} -- id for job to be stopped
        
        Returns:
            [dict] -- []
            
    `get_environment_variables(self, params)`
    :   Get the project level environment variables
        
        Arguments:
            params {dict} -- None
        
        Returns:
            [dict] -- []
            
    `create_environment_variable(self, params)`
    :   Add project level environment variables
        
        Arguments:
            params {dict} -- [dict containing environment variable key pairs]
        
        Returns:
            [dict] -- []
