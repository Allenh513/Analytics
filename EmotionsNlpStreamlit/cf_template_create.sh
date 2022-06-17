export TaskExecutionRole=''
export ECRImageURI=''
export ContainerPort='8501'
export subnet1=''
export subnet2=''
export subnet3=''
export vpcid=''
rm -f final.yaml temp.yaml
( echo "cat <<EOF >final.yaml";
  cat resources_aws_cf.yaml;
) >temp.yaml
. temp.yaml
cat final.yaml