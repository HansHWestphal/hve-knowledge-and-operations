# HVE Local OCR Fallback

**Date:** August 19, 2026  
**Version:** 1.0  
**Status:** Implementation in progress  
**Owner:** Hermes-coder

## Purpose

HVE receives scanned and image-based PDFs through the Telegram knowledge
collector. These files contain no usable PDF text layer, so `pdftotext` alone
cannot create pages for chunking and retrieval.

## Implemented design

The intake pipeline now follows this local-first sequence:

```text
PDF
  -> pdftotext
  -> native text detected: continue normally
  -> no usable text: render pages with pdftoppm
  -> OCR each page with local Tesseract
  -> preserve page boundaries in extracted text
  -> chunk, embed, and index locally
```

Native text remains the fast path. OCR runs on CPU so it does not compete with
Hermes models or Ollama GPU workloads.

## Provenance and operational behavior

Manifests record:

- `extraction_method`: `native_text` or `ocr`
- `ocr_status`: `not_required`, `completed`, `unavailable`, `empty`, or
  `failed`
- `ocr_language`
- `ocr_page_count`

Temporary rendered page images are deleted after each document. Raw PDFs,
OCR text, chunks, manifests, and LanceDB records remain local under
`/hve-library`.

The pipeline also skips a file that disappears between inbox discovery and
manifest creation instead of crashing the intake service.

## Sovereignty boundary

OCR uses no cloud service, Hugging Face request, external API, or LLM. The
embedding stage remains local and is configured to use Ollama. The intake
service is configured for offline model operation and CPU-only OCR/indexing.

Required host packages:

```text
poppler-utils
tesseract-ocr
tesseract-ocr-eng
```

## Validation requirements

The implementation must be validated against:

1. Native text PDFs.
2. Scanned/image-only PDFs.
3. Mixed text and image PDFs.
4. Rotated or skewed pages.
5. Tables and multi-column layouts.
6. PDFs with no readable text.

The raw source must remain preserved even when OCR fails. Failure records must
identify whether the cause was missing OCR tooling, rendering failure, OCR
failure, or empty OCR output.

## Follow-up

Install the required Tesseract packages on the DGX Spark, then process the
currently quarantined scanned PDF and the next two Telegram submissions. A
later enhancement may add local OCR confidence and optional post-OCR cleanup,
but raw OCR remains authoritative input and no cloud OCR is planned.
