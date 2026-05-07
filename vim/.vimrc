" --- Plugin ----
call plug#begin()

" Theme & UI
Plug 'catppuccin/vim', { 'as': 'catppuccin' }
Plug 'vim-airline/vim-airline'
Plug 'ryanoasis/vim-devicons'

" Navigation
Plug 'preservim/nerdtree'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'

" Tools
Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app && npx --yes yarn install' }
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'sheerun/vim-polyglot'
Plug 'jiangmiao/auto-pairs'
Plug 'airblade/vim-gitgutter'

call plug#end()

" --- Shortcut ----
" Press CTRL+N to open/close folder explorer
nnoremap <C-n> :NERDTreeToggle<CR>
" Press Ctrl + p to search for files (p = project/path)
nnoremap <C-p> :Files<CR>
" Press Ctrl + g to search for a word in all files (like VS Code Search)
nnoremap <C-g> :Rg<CR>
" Press Ctrl + b to view currently opened files (buffers)
nnoremap <C-b> :Buffers<CR>

nnoremap <Tab> :Autocomplete<CR>

vmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" --- Command ---
"  use :Prettier for call prettier formatter
command! -nargs=0 Prettier :CocCommand prettier.forceFormatDocument


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
set tabstop=2
set shiftwidth=2
set expandtab

" --- Additional Feature ---  
set mouse=a
set clipboard=unnamedplus
set ignorecase
set smartcase
