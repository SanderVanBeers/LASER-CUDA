#All inputfiles should be in /input/. The filenames have to be their language code
#Aligned bitexts will be in the /output/ directory
while getopts i:o: flag
do
    case "${flag}" in
        i) input_directory=${OPTARG};;
        o) output_directory=${OPTARG};;
    esac
done
docker run --runtime=nvidia --rm -e NVIDIA_VISIBLE_DEVICES=1 -v $input_directory:/input -v $output_directory:/output laser/bitext 
