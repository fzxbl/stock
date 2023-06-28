package main

import (
	_ "github.com/fzxbl/stock/internal/packed"

	"github.com/gogf/gf/v2/os/gctx"

	"github.com/fzxbl/stock/internal/cmd"
)

func main() {
	cmd.Main.Run(gctx.GetInitCtx())
}
