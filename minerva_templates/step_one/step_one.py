from argparse import ArgumentParser
from minerva import Experiment

def predict(experiment, pdf_s3_path, project_name):
  experiment.start()
  print("Step one...")
  print(experiment)
  print()
  print(pdf_s3_path)
  print()
  print(f"Project Name: {project_name}")
  experiment.done()


def main():
    parser = ArgumentParser()

    parser.add_argument(
        "--name", help="experiment name Type: str", required=True)
    parser.add_argument(
        "--project_name", help="minerva project name Type: str", required=True)
    parser.add_argument("--version", help="task version Type: str")
    parser.add_argument(
        "--job_type", help="training|prediction", required=True)

    parser.add_argument("--pdf_s3_path", help="Annotation S3 path")
    
    args = parser.parse_args()

    project_name = args.project_name
    experiment = Experiment(args.name, project_name=project_name)

    job_type = args.job_type

    if job_type == "training":
      pass
    elif job_type == "prediction":
        predict(experiment, args.pdf_s3_path, project_name)
    else:
        raise ValueError("job_type has to either training|prediction")


if __name__ == "__main__":
    main()
