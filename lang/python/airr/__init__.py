"""
Reference library for AIRR schema for Ig/TCR rearrangements
"""

from airr.formats import Rearrangements


def read(filename):
    """Open an AIRR rearrangements file and read its contents"""
    return Rearrangements(filename, False)


def create(filename):
    """Create an empty AIRR rearrangements file"""
    return Rearrangements(filename, True)


def createDerivation(inputFilename, outputFilename, toolEntity, activity,
                     namespace, namespaceURI):
    """Create a derived AIRR rearrangments file, possibly with addl annotation
    fields
    """
    ifile = Rearrangements(inputFilename, False)
    ofile = Rearrangements(outputFilename, True)
    ofile.deriveFrom(ifile)
    ofile.addAnnotationActivity(inputFilename, outputFilename, toolEntity, activity, None, namespace, namespaceURI)
    return [ifile, ofile]


# versioneer-generated
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
