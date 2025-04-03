{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {
    self,
    nixpkgs,
  }: let
    allSystems = ["x86_64-linux"];

    forAllSystems = f:
      nixpkgs.lib.genAttrs allSystems
      (system: f {pkgs = import nixpkgs {inherit system;};});
  in {
    devShells = forAllSystems ({pkgs}: {
      default = let
        python = pkgs.python3.withPackages (ps: with ps; []);
      in
        pkgs.mkShell {
          name = "prototype";

          venvDir = "./.venv";

          postVenvCreation = ''
            unset SOURCE_DATE_EPOCH
            pip install -r ${./requirements.txt}
          '';

          buildInputs = with pkgs; [
            python
            python312Packages.venvShellHook
          ];

          packages = with pkgs; [
            python
            basedpyright
            ruff
          ];

          postShellHook = ''
            unset SOURCE_DATE_EPOCH
          '';
        };
    });
  };
}
