#!/bin/bash
#PBS -N parallel_download
#PBS -q debug-scaling
#PBS -A EVITA
#PBS -l select=10:system=polaris
#PBS -l place=scatter
#PBS -l walltime=1:00:00
#PBS -l filesystems=home:eagle

cd $PBS_O_WORKDIR

# Debugging info
echo "Job started on `hostname` at `date`" > $PBS_O_WORKDIR/job.log

module load conda
conda activate youtubedl
cd /home/ben2002chou/code/audioset-processing-fix

# Debugging info
env > $PBS_O_WORKDIR/env.log

# Assuming 1 process per node
rpn=1
procs=$((PBS_NODES*rpn))

# Loop to launch the Python script on each node with a different offset value
for i in $(seq 0 $((procs - 1)))
do
    # Use pbsdsh to launch the Python script on each node
    pbsdsh -n $i -- python3 process_unbalanced_1M.py download-all-multithreaded --offset $i &

    # Debugging info
    echo "Launched script on node $i with offset $i" >> $PBS_O_WORKDIR/launch.log
done

# Wait for all background processes to finish
wait

conda deactivate

# Debugging info
echo "Job ended on `hostname` at `date`" >> $PBS_O_WORKDIR/job.log
