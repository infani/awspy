from awspy.ssm import ssm


def test_ssm_get():
    name = 'TestGetParameter'
    cli = ssm()
    res = cli.getParameter(name)
    assert res['Parameter']['Name'] == name