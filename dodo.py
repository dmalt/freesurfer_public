import os

from doit import get_var

config = {
    "subject": get_var("subject", "bert"),
    "recon_all_cmd": get_var("recon_all_cmd", "-all"),
}
bem_dir = os.environ["SUBJECTS_DIR"] + "/{subject}/bem".format(**config)


def task_fsf_recon_all():
    """
    Perform cortical reconstruction using FREESURFER recon-all command

    The command being run is
    $ recon-all -s {subject} {recon_all_cmd}


    Examples
    --------
    Regular run:
    >>> fsf_recon_all subject=sub-01 recon_all_cmd='-all -i /anat/sub-01_T1w.nii.gz'

    Parallel run on 8 cores:
    >>> fsf_recon_all subject=sub-01 recon_all_cmd='-all -i /anat/sub-01_T1w.nii.gz'\
    -parallel -openmp 8


    Notes
    -----
    In case no command-line variables are set, runs for default freesurfer
    subject 'bert' for testing purposes. For a normal run 'subject'
    and 'recon_all_cmd' command-line variables must be set.
    For 'recon_all_cmd' options see FREESURFER recon-all documentation.

    Unlike the recon-all command, this task doesn't fail if the target subject
    directory exists. Instead, it does nothing for the ease of recomputing.

    """
    return dict(
        uptodate=[True],
        actions=["recon-all -s {subject} {recon_all_cmd}".format(**config)],
        targets=[os.environ["SUBJECTS_DIR"] + "/{subject}".format(**config)],
    )


def task_make_bem_surfaces():
    """
    Make BEM surfaces using watershed algorithm using MNE-Python

    The command being run is
    $ mne watershed_bem -o -s {subject} --copy

    """
    return dict(
        uptodate=[True],
        actions=["mne watershed_bem -o -s {subject} --copy".format(**config)],
        targets=[
            f"{bem_dir}" + "/{subject}-head.fif".format(**config),
            f"{bem_dir}" + "/outer_skin.surf".format(**config),
            f"{bem_dir}" + "/inner_skull.surf".format(**config),
            f"{bem_dir}" + "/outer_skull.surf".format(**config),
            f"{bem_dir}" + "/brain.surf".format(**config),
        ],
    )


def task_make_scalp_surfaces():
    """
    Make BEM scalp surfaces using MNE-Python

    The command being run is
    $ mne make_scalp_surfaces -o -f -s {subject}

    """
    return dict(
        uptodate=[True],
        actions=["mne make_scalp_surfaces -o -f -s {subject}".format(**config)],
        targets=[
            f"{bem_dir}" + "/{subject}-head-sparse.fif".format(**config),
            f"{bem_dir}" + "/{subject}-head-medium.fif".format(**config),
            f"{bem_dir}" + "/{subject}-head-dense.fif".format(**config),
        ],
    )
