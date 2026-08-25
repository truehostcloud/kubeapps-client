# Regenerating this client

Everything in `kubeapps_client/`, `docs/` and `test/` is generator output.
Do not hand-edit it. If something is wrong, fix the spec or the generator
invocation and regenerate.

## Source of truth

`kubeapps-apis.swagger.json` is the spec this tree was generated from, taken
from the Kubeapps project:

```
https://raw.githubusercontent.com/vmware-tanzu/kubeapps/main/cmd/kubeapps-apis/docs/kubeapps-apis.swagger.json
```

Refresh it from upstream when you want newly added endpoints, then regenerate.

## Regenerating

Generator version is pinned in `.swagger-codegen/VERSION`.

With Docker:

```bash
docker run --rm -v "${PWD}:/local" \
  swaggerapi/swagger-codegen-cli-v3:3.0.46 generate \
  -i /local/kubeapps-apis.swagger.json \
  -l python \
  -o /local \
  --additional-properties packageName=kubeapps_client,packageVersion=1.0.1
```

With the standalone jar, if you already have a JVM:

```bash
curl -sSLO https://repo1.maven.org/maven2/io/swagger/codegen/v3/swagger-codegen-cli/3.0.46/swagger-codegen-cli-3.0.46.jar
java -jar swagger-codegen-cli-3.0.46.jar generate \
  -i kubeapps-apis.swagger.json \
  -l python \
  -o . \
  --additional-properties packageName=kubeapps_client,packageVersion=1.0.1
```

Bump `packageVersion` when cutting a release and tag the commit, because
consumers pin this repo by tag.

## Consuming the client

The generated `Configuration` takes no constructor arguments. Set the fields
after construction:

```python
configuration = Configuration()
configuration.host = "https://kubeapps.example.com/apis"
configuration.api_key = {"Authorization": token}
configuration.api_key_prefix = {"Authorization": "Bearer"}
```

Earlier revisions of this repo hand-patched the constructor to accept these
as arguments. That patch is gone. Assign the attributes instead so this tree
stays reproducible from the spec.
