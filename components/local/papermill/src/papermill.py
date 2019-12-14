import argparse
import papermill as pm

def main(input_notebook, output_notebook, parameters):
    pm.execute_notebook(
        input_path=input_path,
        output_path=output_path,
        parameters=parameters
    )

def parser_args():
    parser = argparse.ArgumentParser(description='Papermill notebook executor')
    parser.add_argument('--input-notebook', type=str,
                        help='Path to the notebook to be executed.')
    parser.add_argument('--output-notebook', type=str,
                        help='Path to write the executed notebook.')
    parser.add_argument('--parameters', type=str,
                        help='Path to parameters file.')

if __name__ == "__main__":
    args = parser_args()
    main(args.input_notebook, args.output_notebook, args.parameters)
