;; Batch export Org slides with org-re-reveal and color link support.

(let* ((repo-root (or (getenv "REPO_ROOT") default-directory))
       (re-reveal-path (or (getenv "RE_REVEAL_PATH")
                           (expand-file-name "~/.emacs.d/.local/straight/repos/org-re-reveal"))))
  (add-to-list 'load-path re-reveal-path)
  (require 'org)
  (require 'org-re-reveal)

  ;; Keep compatibility with existing [[color:...][...]] links used in course files.
  (org-link-set-parameters
   "color"
   :export
   (lambda (color description backend _com)
     (let ((txt (or description color)))
       (cond
        ((eq backend 'html)
         (let* ((rgb (assoc-string color color-name-rgb-alist t))
                (r (and rgb (* 255.0 (/ (nth 1 rgb) 65535.0))))
                (g (and rgb (* 255.0 (/ (nth 2 rgb) 65535.0))))
                (b (and rgb (* 255.0 (/ (nth 3 rgb) 65535.0)))))
           (if rgb
               (format "<span style=\"color: rgb(%d,%d,%d)\">%s</span>"
                       (truncate r) (truncate g) (truncate b) txt)
             (format "<span style=\"color: %s\">%s</span>" color txt))))
        ((eq backend 'latex)
         (format "\\textcolor{%s}{%s}" color txt))
        (t txt)))))

  (let ((org-file (car command-line-args-left)))
    (unless org-file
      (error "Missing org file path argument"))
    (find-file org-file)
    (org-re-reveal-export-to-html)
    (princ (format "export-ok %s\n" org-file))))
