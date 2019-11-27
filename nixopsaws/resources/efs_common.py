import boto3
import nixops.util
import nixopsaws.ec2_utils

class EFSCommonState():

    _client = None
    profile = nixops.util.attr_property("ec2.profile", None)

    def _get_client(self, access_key_id=None, region=None, profile=None):
        if self._client: return self._client

        (access_key_id, secret_access_key) = nixopsaws.ec2_utils.fetch_aws_secret_key(access_key_id or self.access_key_id)

        self._client = boto3.session.Session(profile_name=self.profile).client('efs',
                           region_name=region or self.region,
                           aws_access_key_id=access_key_id,
                           aws_secret_access_key=secret_access_key
                       )

        return self._client
