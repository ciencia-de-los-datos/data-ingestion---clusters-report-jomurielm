"""
Calificación del laboratorio
-----------------------------------------------------------------------------------------
"""

import sys

import pregunta


def test_01():
    assert pregunta.ingest_data().cluster.to_list() == list(range(1, 14))


def test_02():
    assert pregunta.ingest_data().cantidad_de_palabras_clave.to_list() == [
        105,
        102,
        89,
        60,
        52,
        51,
        42,
        38,
        35,
        27,
        22,
        22,
        17,
    ]


def test_03():
    assert pregunta.ingest_data().porcentaje_de_palabras_clave.to_list() == [
        15.9,
        15.4,
        13.4,
        9.1,
        7.9,
        7.7,
        6.3,
        5.7,
        5.3,
        4.1,
        3.3,
        3.3,
        2.6,
    ]


def test_04():

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[0]
        == "maximum power point tracking, fuzzy-logic based control, photo voltaic (pv), photo-voltaic system, differential evolution algorithm, evolutionary algorithm, double-fed induction generator (dfig), ant colony optimisation, photo voltaic array, firefly algorithm, partial shade"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[1]
        == "support vector machine, long short-term memory, back-propagation neural network, convolution neural network, speed wind prediction, energy consumption, wind power forecasting, extreme learning machine, recurrent-neural-network (rnn), radial basis function (rbf) networks, wind farm"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[2]
        == "smart grid, wind power, reinforcement learning, energy management, energy efficiency, solar energy, deep reinforcement learning, demand-response (dr), internet of things, energy harvester, q-learning"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[3]
        == "wind turbine, fault diagnosis, biodiesel, failure detection, response-surface methodology, condition monitoring, load forecasting, energy consumption forecast, anomalies detection, optimization-based algorithm, supervisory control and data acquisition"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[4]
        == "electric vehicle, lithium-ion batteries, state of charge, state of health, hybrid-electric vehicle, energy management strategies, energy management system, remaining useful life, battery management system, transfer learning, hybrid energy storage"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[5]
        == "particle swarm optimization, distribute generation, solar irradiance, artificial bee colonies, energy storage systems, bat algorithm, gravitational search algorithm, distributed system, multi-objective swarm optimization (mopso), optimal power-flow (opf), load-frequency control"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[6]
        == "multi-objective optimization, energy storage, economic dispatch, non-dominated sorting genetic algorithm, sensitive analysis, hybrid renewable energy source, plug-in electric vehicle, combined-heat and power, multi-objective genetic algorithm, unit-commitment, dc-dc converters"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[7]
        == "genetic algorithm, demand-side management, energy-saving, hybrid electric system (hes), wind turbine blade, data-driven modelling, simulated annealing, solar forecasting, geographic information system, renewable energy system, cogeneration"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[8]
        == "anfis, global solar irradiance, solar irradiance forecast, genetic programing, islanding detection, expert system, distributed networks, evolutionary computation, wavelet-based neural network, root mean square errors, virtual power plant"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[9]
        == "micro grid, multi-agent systems, distributed energy resource, batteries energy storage system, dc micro grid, pitch-control, droop control, hybrid ac/dc microgrid, voltage regulation, superconducting magnetic energy storage, distributed-control"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[10]
        == "hydrogen, biochar, biomass, biogas, microbial fuel cell, gasification, biofuel, ethanol, engine performance, pyrolysis, anaerobic digester"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[11]
        == "state of charge (soc) estimation, radial basis function, short-term load forecasting, computational fluid dynamics, generalized-regression neural network, monte-carlo simulation, multiple linear regression, power generation, nonlinear auto-regressive exogenous (narx) model neural networks, surrogate model, extreme gradient boosting"
    )

    assert (
        pregunta.ingest_data().principales_palabras_clave.to_list()[12]
        == "pem fuel cell, solid-oxide fuel cell, deep-belief networks, energy optimisation, particles-size distributions, biomass gasification, exergy, battery management, hydrogen production, numeric simulation, system-identification"
    )


test = {
    "01": test_01,
    "02": test_02,
    "03": test_03,
    "04": test_04,
}[sys.argv[1]]

test()
