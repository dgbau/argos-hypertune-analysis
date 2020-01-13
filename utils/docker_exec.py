import os

def trial_exec(params):
    os.system(f'docker run --rm -v $PWD/scripts:/scripts -it dbitz/argos-cpfa:v1 bash \
        -c "python3 /scripts/runner.py \
        -ProbabilityOfSwitchingToSearching {params["ProbabilityOfSwitchingToSearching"]} \
        -ProbabilityOfReturningToNest {params["ProbabilityOfReturningToNest"]} \
        -UninformedSearchVariation {params["UninformedSearchVariation"]} \
        -RateOfInformedSearchDecay {params["RateOfInformedSearchDecay"]} \
        -RateOfSiteFidelity {params["RateOfSiteFidelity"]} \
        -RateOfLayingPheromone {params["RateOfLayingPheromone"]} \
        -RateOfPheromoneDecay {params["RateOfPheromoneDecay"]} \
        -FoodDistribution {params["FoodDistribution"]} \
        -ParamSource {params["ParamSource"]} \
        -PrintFinalScore 1 \
        -PrintParams 0" \
    | sed "s/\x1b\[[0-9;]*[a-zA-Z]//g" >> docker_output.csv')
