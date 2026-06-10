# Pickle Deserialization

## What Is It
pickle is Python's built-in serialization module. Serialization means converting a Python object (a list, a dict, a class instance) into bytes so you can save it to disk or send it over a network. Deserialization is the reverse — bytes back into a  Python object.

```python
import pickle

data = {"user": "alice", "role": "admin"}
raw = pickle.dumps(data)   # Python object → bytes
obj = pickle.loads(raw)    # bytes → Python object
```

## How the Attack Works
JSON only stores data. Pickle stores instructions — specifically, instructions on how to reconstruct an object. When Python unpickles something, it executes those instructions.
An attacker can craft a pickle payload where the "reconstruction instructions" are actually os.system("rm -rf /") or a reverse shell. Python will execute that code without question the moment you call pickle.loads().
The mechanism: any class can define a __reduce__ method that returns a callable and its arguments. Pickle will call that callable during unpickle. There is no sandboxing.

## Risks
- reverse shell
- data deletion
- read environment variables, steal API keys, read database credentials from config files
- establish persistence (create backdoor files)
- move laterally to other internal services


## Mitigations
- Use JSON for untrusted data
- HMAC-sign if you must use pickle
- Never accept pickle from user input / external sources (which is really a restatement of #1 but worth saying explicitly)  

## CVE
- CVE-2019-6446 — NumPy. numpy.load() accepted pickle by default when loading .npy files. A crafted file triggered arbitrary code execution. Fixed by changing allow_pickle default to False in NumPy 1.16.3.
- Celery (no single CVE — security advisory) — Celery used pickle as its default task serializer. An attacker with access to the message broker (Redis, RabbitMQ) could inject malicious pickle payloads and execute code on any worker. Celery changed the  default to JSON and documented this as a critical configuration requirement.