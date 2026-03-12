" --- Plugin ----
call plug#begin()
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && npx --yes yarn install' }
call plug#end()

" --- Basic view ---
syntax on
set number
set relativenumber
set cursorline
set termguicolors
set fillchars=eob:-

" Colors
highlight LineNr ctermfg=grey guifg=#808080
highlight CursorLineNr ctermfg=yellow guifg=#FFFF00
colorscheme catppuccin_macchiato

" --- Tab & Indentation ---  
set tabstop=4
set shiftwidth=4
set expandtab

" --- Additional Feature ---  
set mouse=a
set clipboard=unnamedplus
set ignorecase
set smartcase
