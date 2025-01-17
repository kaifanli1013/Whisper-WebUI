from typing import Optional
import os

from modules.whisper.faster_whisper_inference import FasterWhisperInference
from modules.whisper.whisper_Inference import WhisperInference
from modules.whisper.insanely_fast_whisper_inference import InsanelyFastWhisperInference
from modules.whisper.whisper_base import WhisperBase


class WhisperFactory:
    @staticmethod
    def create_whisper_inference(
        whisper_type: str,
        whisper_model_dir: Optional[str] = None,
        faster_whisper_model_dir: Optional[str] = None,
        insanely_fast_whisper_model_dir: Optional[str] = None,
        diarization_model_dir: Optional[str] = None,
        output_dir: Optional[str] = None,
    ) -> "WhisperBase":
        """
        Create a whisper inference class based on the provided whisper_type.

        Parameters
        ----------
        whisper_type : str
            The type of Whisper implementation to use. Supported values (case-insensitive):
            - "faster-whisper": https://github.com/openai/whisper
            - "whisper": https://github.com/openai/whisper
            - "insanely-fast-whisper": https://github.com/Vaibhavs10/insanely-fast-whisper
        whisper_model_dir : str
            Directory path for the Whisper model.
        faster_whisper_model_dir : str
            Directory path for the Faster Whisper model.
        insanely_fast_whisper_model_dir : str
            Directory path for the Insanely Fast Whisper model.
        diarization_model_dir : str
            Directory path for the diarization model.
        output_dir : str
            Directory path where output files will be saved.

        Returns
        -------
        WhisperBase
            An instance of the appropriate whisper inference class based on the whisper_type.
        """
        # Temporal fix of the bug : https://github.com/jhj0517/Whisper-WebUI/issues/144
        os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

        whisper_type = whisper_type.lower().strip()

        faster_whisper_typos = ["faster_whisper", "faster-whisper", "fasterwhisper"]
        whisper_typos = ["whisper"]
        insanely_fast_whisper_typos = [
            "insanely_fast_whisper", "insanely-fast-whisper", "insanelyfastwhisper",
            "insanely_faster_whisper", "insanely-faster-whisper", "insanelyfasterwhisper"
        ]

        if whisper_type in faster_whisper_typos:
            return FasterWhisperInference(
                model_dir=faster_whisper_model_dir,
                output_dir=output_dir,
                diarization_model_dir=diarization_model_dir
            )
        elif whisper_type in whisper_typos:
            return WhisperInference(
                model_dir=whisper_model_dir,
                output_dir=output_dir,
                diarization_model_dir=diarization_model_dir
            )
        elif whisper_type in insanely_fast_whisper_typos:
            return InsanelyFastWhisperInference(
                model_dir=insanely_fast_whisper_model_dir,
                output_dir=output_dir,
                diarization_model_dir=diarization_model_dir
            )
        else:
            return FasterWhisperInference(
                model_dir=faster_whisper_model_dir,
                output_dir=output_dir,
                diarization_model_dir=diarization_model_dir
            )
