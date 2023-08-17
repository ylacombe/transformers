# Copyright 2020 The HuggingFace Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TYPE_CHECKING

from ...utils import  _LazyModule, OptionalDependencyNotAvailable, is_tokenizers_available
from ...utils import is_torch_available




_import_structure = {
    "configuration_seamless_m4t": ["SEAMLESS_M4T_PRETRAINED_CONFIG_ARCHIVE_MAP", "SeamlessM4TConfig"],
    "tokenization_seamless_m4t": ["SeamlessM4TTokenizer"],
}

try:
    if not is_tokenizers_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["tokenization_seamless_m4t_fast"] = ["SeamlessM4TTokenizerFast"]

try:
    if not is_torch_available():
        raise OptionalDependencyNotAvailable()
except OptionalDependencyNotAvailable:
    pass
else:
    _import_structure["modeling_seamless_m4t"] = [
        "SEAMLESS_M4T_PRETRAINED_MODEL_ARCHIVE_LIST",
        "SeamlessM4TForMaskedLM",
        "SeamlessM4TForCausalLM",
        "SeamlessM4TForMultipleChoice",
        "SeamlessM4TForQuestionAnswering",
        "SeamlessM4TForSequenceClassification",
        "SeamlessM4TForTokenClassification",
        "SeamlessM4TLayer",
        "SeamlessM4TModel",
        "SeamlessM4TPreTrainedModel",
        "load_tf_weights_in_seamless_m4t",
    ]




if TYPE_CHECKING:
    from .configuration_seamless_m4t import SEAMLESS_M4T_PRETRAINED_CONFIG_ARCHIVE_MAP, SeamlessM4TConfig
    from .tokenization_seamless_m4t import SeamlessM4TTokenizer

    try:
        if not is_tokenizers_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .tokenization_seamless_m4t_fast import SeamlessM4TTokenizerFast

    try:
        if not is_torch_available():
            raise OptionalDependencyNotAvailable()
    except OptionalDependencyNotAvailable:
        pass
    else:
        from .modeling_seamless_m4t import (
            SEAMLESS_M4T_PRETRAINED_MODEL_ARCHIVE_LIST,
            SeamlessM4TForMaskedLM,
            SeamlessM4TForCausalLM,
            SeamlessM4TForMultipleChoice,
            SeamlessM4TForQuestionAnswering,
            SeamlessM4TForSequenceClassification,
            SeamlessM4TForTokenClassification,
            SeamlessM4TLayer,
            SeamlessM4TModel,
            SeamlessM4TPreTrainedModel,
            load_tf_weights_in_seamless_m4t,
        )



else:
    import sys

    sys.modules[__name__] = _LazyModule(__name__, globals()["__file__"], _import_structure, module_spec=__spec__)