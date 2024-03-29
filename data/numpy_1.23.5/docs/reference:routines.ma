{
  "aliases": [],
  "arbitrary": [
    {
      "children": [
        {
          "args": "numpy",
          "children": [],
          "name": "currentmodule",
          "options": {},
          "type": "mystDirective",
          "value": ""
        }
      ],
      "level": 0,
      "target": "routines.ma",
      "title": "Masked array operations",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.MaskType"
        }
      ],
      "level": 1,
      "target": null,
      "title": "Constants",
      "type": "Section"
    },
    {
      "children": [],
      "level": 1,
      "target": null,
      "title": "Creation",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.masked_array\n    ma.array\n    ma.copy\n    ma.frombuffer\n    ma.fromfunction\n\n    ma.MaskedArray.copy\n    ma.diagflat"
        }
      ],
      "level": 2,
      "target": null,
      "title": "From existing data",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.empty\n    ma.empty_like\n    ma.masked_all\n    ma.masked_all_like\n    ma.ones\n    ma.ones_like\n    ma.zeros\n    ma.zeros_like"
        },
        {
          "type": "Transition"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Ones and zeros",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.all\n    ma.any\n    ma.count\n    ma.count_masked\n    ma.getmask\n    ma.getmaskarray\n    ma.getdata\n    ma.nonzero\n    ma.shape\n    ma.size\n    ma.is_masked\n    ma.is_mask\n    ma.isMaskedArray\n    ma.isMA\n    ma.isarray\n    ma.isin\n    ma.in1d\n    ma.unique\n\n\n    ma.MaskedArray.all\n    ma.MaskedArray.any\n    ma.MaskedArray.count\n    ma.MaskedArray.nonzero\n    ma.shape\n    ma.size"
        },
        {
          "type": "code",
          "value": ".. autosummary:: \n    ma.MaskedArray.data\n    ma.MaskedArray.mask\n    ma.MaskedArray.recordmask"
        },
        {
          "type": "Transition"
        }
      ],
      "level": 1,
      "target": null,
      "title": "Inspecting the array",
      "type": "Section"
    },
    {
      "children": [],
      "level": 1,
      "target": null,
      "title": "Manipulating a MaskedArray",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.ravel\n    ma.reshape\n    ma.resize\n\n    ma.MaskedArray.flatten\n    ma.MaskedArray.ravel\n    ma.MaskedArray.reshape\n    ma.MaskedArray.resize"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Changing the shape",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.swapaxes\n    ma.transpose\n\n    ma.MaskedArray.swapaxes\n    ma.MaskedArray.transpose"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Modifying axes",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.atleast_1d\n    ma.atleast_2d\n    ma.atleast_3d\n    ma.expand_dims\n    ma.squeeze\n\n    ma.MaskedArray.squeeze\n\n    ma.stack\n    ma.column_stack\n    ma.concatenate\n    ma.dstack\n    ma.hstack\n    ma.hsplit\n    ma.mr_\n    ma.row_stack\n    ma.vstack"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Changing the number of dimensions",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.concatenate\n    ma.stack\n    ma.vstack\n    ma.hstack\n    ma.dstack\n    ma.column_stack\n    ma.append"
        },
        {
          "type": "Transition"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Joining arrays",
      "type": "Section"
    },
    {
      "children": [],
      "level": 1,
      "target": null,
      "title": "Operations on masks",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.make_mask\n    ma.make_mask_none\n    ma.mask_or\n    ma.make_mask_descr"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Creating a mask",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.getmask\n    ma.getmaskarray\n    ma.masked_array.mask"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Accessing a mask",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.ndenumerate\n    ma.flatnotmasked_contiguous\n    ma.flatnotmasked_edges\n    ma.notmasked_contiguous\n    ma.notmasked_edges\n    ma.clump_masked\n    ma.clump_unmasked"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Finding masked data",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.mask_cols\n    ma.mask_or\n    ma.mask_rowcols\n    ma.mask_rows\n    ma.harden_mask\n    ma.soften_mask\n\n    ma.MaskedArray.harden_mask\n    ma.MaskedArray.soften_mask\n    ma.MaskedArray.shrink_mask\n    ma.MaskedArray.unshare_mask"
        },
        {
          "type": "Transition"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Modifying a mask",
      "type": "Section"
    },
    {
      "children": [],
      "level": 1,
      "target": null,
      "title": "Conversion operations",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.asarray\n    ma.asanyarray\n    ma.fix_invalid\n    ma.masked_equal\n    ma.masked_greater\n    ma.masked_greater_equal\n    ma.masked_inside\n    ma.masked_invalid\n    ma.masked_less\n    ma.masked_less_equal\n    ma.masked_not_equal\n    ma.masked_object\n    ma.masked_outside\n    ma.masked_values\n    ma.masked_where"
        }
      ],
      "level": 2,
      "target": null,
      "title": "> to a masked array",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.compress_cols\n    ma.compress_rowcols\n    ma.compress_rows\n    ma.compressed\n    ma.filled\n\n    ma.MaskedArray.compressed\n    ma.MaskedArray.filled"
        }
      ],
      "level": 2,
      "target": null,
      "title": "> to a ndarray",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.MaskedArray.tofile\n    ma.MaskedArray.tolist\n    ma.MaskedArray.torecords\n    ma.MaskedArray.tobytes"
        }
      ],
      "level": 2,
      "target": null,
      "title": "> to another object",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.common_fill_value\n    ma.default_fill_value\n    ma.maximum_fill_value\n    ma.minimum_fill_value\n    ma.set_fill_value\n\n    ma.MaskedArray.get_fill_value\n    ma.MaskedArray.set_fill_value"
        },
        {
          "type": "code",
          "value": ".. autosummary:: \n    ma.MaskedArray.fill_value"
        },
        {
          "type": "Transition"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Filling a masked array",
      "type": "Section"
    },
    {
      "children": [],
      "level": 1,
      "target": null,
      "title": "Masked arrays arithmetic",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.anom\n    ma.anomalies\n    ma.average\n    ma.conjugate\n    ma.corrcoef\n    ma.cov\n    ma.cumsum\n    ma.cumprod\n    ma.mean\n    ma.median\n    ma.power\n    ma.prod\n    ma.std\n    ma.sum\n    ma.var\n\n    ma.MaskedArray.anom\n    ma.MaskedArray.cumprod\n    ma.MaskedArray.cumsum\n    ma.MaskedArray.mean\n    ma.MaskedArray.prod\n    ma.MaskedArray.std\n    ma.MaskedArray.sum\n    ma.MaskedArray.var"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Arithmetic",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.argmax\n    ma.argmin\n    ma.max\n    ma.min\n    ma.ptp\n    ma.diff\n\n    ma.MaskedArray.argmax\n    ma.MaskedArray.argmin\n    ma.MaskedArray.max\n    ma.MaskedArray.min\n    ma.MaskedArray.ptp"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Minimum/maximum",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.argsort\n    ma.sort\n    ma.MaskedArray.argsort\n    ma.MaskedArray.sort"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Sorting",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.diag\n    ma.dot\n    ma.identity\n    ma.inner\n    ma.innerproduct\n    ma.outer\n    ma.outerproduct\n    ma.trace\n    ma.transpose\n\n    ma.MaskedArray.trace\n    ma.MaskedArray.transpose"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Algebra",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.vander\n    ma.polyfit"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Polynomial fit",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.around\n    ma.clip\n    ma.round\n\n    ma.MaskedArray.clip\n    ma.MaskedArray.round"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Clipping and rounding",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.intersect1d\n    ma.setdiff1d\n    ma.setxor1d\n    ma.union1d"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Set operations",
      "type": "Section"
    },
    {
      "children": [
        {
          "type": "code",
          "value": ".. autosummary:: \n    :toctree:generated/\n    ma.allequal\n    ma.allclose\n    ma.apply_along_axis\n    ma.apply_over_axes\n    ma.arange\n    ma.choose\n    ma.ediff1d\n    ma.indices\n    ma.where"
        }
      ],
      "level": 2,
      "target": null,
      "title": "Miscellanea",
      "type": "Section"
    }
  ],
  "content": {},
  "example_section_data": {
    "children": [],
    "level": 0,
    "target": null,
    "title": null,
    "type": "Section"
  },
  "item_file": null,
  "item_line": null,
  "item_type": null,
  "ordered_sections": [],
  "references": null,
  "see_also": [],
  "signature": {
    "type": "Signature",
    "value": null
  },
  "type": "DocBlob"
}