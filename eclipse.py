import base64



# EXAMPLE  ENCODING  base64
import base64

sample_string = "Hello World!"
sample_string_bytes = sample_string.encode("ascii")

base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Encoded string: {base64_string}")







#  EXAMPLE  DECODING  BASE 64
base64_string ="SGVsbG8gV29ybGQh"
base64_bytes = base64_string.encode("ascii")


# base64bytes contains polled strings


decoded_frameset = base64.b64decode(base64_bytes)
sample_string = decoded_frameset.decode("ascii")

print(f"Decoded string: {sample_string}")
