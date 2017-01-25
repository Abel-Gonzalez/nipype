# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..surface import LabelMapSmoothing


def test_LabelMapSmoothing_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    gaussianSigma=dict(argstr='--gaussianSigma %f',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    inputVolume=dict(argstr='%s',
    position=-2,
    ),
    labelToSmooth=dict(argstr='--labelToSmooth %d',
    ),
    maxRMSError=dict(argstr='--maxRMSError %f',
    ),
    numberOfIterations=dict(argstr='--numberOfIterations %d',
    ),
    outputVolume=dict(argstr='%s',
    hash_files=False,
    position=-1,
    ),
    terminal_output=dict(nohash=True,
    ),
    )
    inputs = LabelMapSmoothing.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_LabelMapSmoothing_outputs():
    output_map = dict(outputVolume=dict(position=-1,
    ),
    )
    outputs = LabelMapSmoothing.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
