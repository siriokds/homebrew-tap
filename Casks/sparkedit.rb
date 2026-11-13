cask "sparkedit" do
  version "2.0.0,183"
  sha256 "e1e907321fa0142c106ec2b0d37015c746d9ced61650f53f61817764402724ca"

  url "https://github.com/siriokds/homebrew-tap/releases/download/sparkedit-#{version.csv.first}-#{version.csv.second}/SparkEdit-#{version.csv.first}-#{version.csv.second}.zip"
  name "SparkEdit"
  desc "Text editor whose tabs are miniatures of their pages"
  homepage "https://github.com/siriokds/homebrew-tap"

  depends_on arch: :arm64
  depends_on macos: :sonoma

  app "SparkEdit.app"
  # spk, as CotEditor's cot: `spk file` opens the file in SparkEdit.
  binary "#{appdir}/SparkEdit.app/Contents/SharedSupport/bin/spk"

  uninstall quit: "com.siriokds.sparkedit"

  # No zap: SparkEdit's folder holds the user's notes and session, never deleted by Homebrew.

  caveats <<~EOS
    SparkEdit is not notarized by Apple. Open it once from Applications: macOS
    stops it; then System Settings > Privacy & Security, "Open Anyway".
    Until then the spk command is stopped too.

    In the shell: spk file opens the file in SparkEdit (spk -h for the rest).
  EOS
end
