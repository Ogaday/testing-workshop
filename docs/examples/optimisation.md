The shadow trading package includes an interface to [Optuna](https://optuna.org/), allowing you to run optimisations over STE strategies. Typical usage would be to find a set of tunable parameters that maximises the gross margin of a strategy over a particular time window during backtesting.

The following code runs 100 trials of the simple peaker simulation with different values of the `sell_price` parameter. It requires an objective function to be defined: this will execute the simulation with the given parameters and return the gross margin. You can view the output of all the trials using [Optuna dashboard](https://optuna-dashboard.readthedocs.io/en/latest/index.html).

``` python
--8<-- "examples/03_simple_optimisation.py:9"
```

Optimisation runs can also be executed using the `ste optimiser` CLI. To do this, define the `OptimiserJob` object as a YAML file, for example:
```yaml
n_trials: 10
start: 2023-01-01 00:00
end: 2023-01-31 23:00
parameters:
  - name: sell_price
    type: float
    low: 0
    high: 300
# Adjust this to point to your objective function
objective_function: your_python_package.run_simulation
```

Then run the optimisation job using the CLI:
```bash
ste optimiser local /path/to/optimisation_job.yaml \
    --storage-url=sqlite:///simple-peaker.db \
    --n-parallel=4
```

Look at the optimisation output using:
```bash
optuna-dashboard sqlite:///simple-peaker.db
```

## Distributed optimisation

Distributed optimisation can be run on AzureML, for example:
```bash
ste optimiser azureml /path/to/optimisation_job.yaml \
    --storage-url="mysql+mysqlconnector://{username}:{password}@mysql-server-stg-001.mysql.database.azure.com:3306/optimisation?ssl_ca=/etc/ssl/certs/DigiCert_Global_Root_CA.pem" \
    --n-parallel=4 \
    --subscription-id=c69953cb-ba4b-4849-b72c-1f971a1ef9c3 \
    --resource-group=rg-azureml-staging-uksouth \
    --workspace-name=workspace-ml-stg-001 \
    --compute-target=ste-compute \
    --environment-name=shadow-trading@latest \
    --n-local-jobs=4
```

In this case, a MySQL database that is accessible to all of the AzureML workers will store the optimisation results. The `n_parallel` parameter controls the number of AzureML workers, while `n_local_jobs` specifies how many concurrent jobs can run on each worker. The command above will therefore run up to 16 concurrent optimisation jobs (4 workers * 4 local jobs per worker). The `environment_name` parameter specifies the name of the AzureML environment that will be used to run the optimisation jobs - this can be created by the CI pipeline for your project.
