# Security Policy

## Security advisories

Advisories for MikoOS security vulnerabilities are reported on the
developer's mailing list. A public archive can be consulted on
https://lists.mikoos.org/mailman/listinfo/mikoos

MikoOS itself has a CPE to track its published vulnerabilities:
https://nvd.nist.gov/products/cpe/search/results?namingFormat=2.3&keyword=mikoos

The MikoOS project provides some ways for its users to track known
vulnerabilites in the packages included in the generated images, see:
- https://nightly.mikoos.org/manual.html#_details_about_packages

In addition, detailed informations for all packages integrated with MikoOS
are updated daily on the following public web pages:
- https://security.mikoos.org/
- https://autobuild.mikoos.org/stats/

## Reporting a Vulnerability

To report a security vulnerability found in the MikoOS build system itself,
please send an email to [security@mikoos.org](mailto:security@mikoos.org).

This is a private mailing list contacting the MikoOS maintainers only.

## Vulnerabilities in packages

MikoOS is a build system that cross-compiles packages from third-party
sources. The MikoOS developers are not responsible for security
vulnerabilities in these packages. Such vulnerabilities should be reported
directly to the upstream project that maintains the affected package.

When vulnerabilities are fixed upstream, send a patch to update the affected
packages in MikoOS.
