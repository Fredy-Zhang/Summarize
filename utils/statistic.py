import torch
from fvcore.nn import FlopCountAnalysis, parameter_count
from functools import wraps


def analyze_model(output_file=None):
    def decorator(func):
        @wraps(func)
        def wrapper(model, input_tensor, *args, **kwargs):
            # Parameter details
            details = ["| Name | #Elements | Shape |",
                       "|:---------------|:---------------------|:---------------------|"]
            total_params = sum(p.numel() for p in model.parameters())
            details.append(f"| model | {total_params} | Total |")

            for name, param in model.named_parameters():
                details.append(f"| {name} | {param.numel()} | {list(param.size())} |")

            # FLOPs calculation
            if input_tensor is not None:
                try:
                    flops = FlopCountAnalysis(model, input_tensor).total()
                    details.append(f"FLOPs: {flops}")
                except Exception as e:
                    details.append(f"Error calculating FLOPs: {e}")

            # Output the details
            output = "\n".join(details)
            if output_file:
                with open(output_file, "w") as file:
                    file.write(output + "\n")
            else:
                print(output)

            # Proceed with the actual function
            return func(model, input_tensor, *args, **kwargs)

        return wrapper

    return decorator
