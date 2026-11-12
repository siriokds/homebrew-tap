class Hexa < Formula
  desc "Hex editor for the terminal: find bytes, replace, go to, checksums"
  homepage "https://github.com/siriokds/homebrew-tap"
  version "0.2.1"

  depends_on arch: :arm64
  depends_on :macos

  # The program already built: nothing is compiled on install.
  on_macos do
    on_arm do
      url "https://github.com/siriokds/homebrew-tap/releases/download/hexa-#{version}/hexa-#{version}-macos-arm64.tar.gz"
      sha256 "ec50d642af9c2d7be0a17699dfe1749eff47c2f56c7cdcc608323fdc5aa1876d"
    end
  end

  def install
    bin.install "hexa"
  end

  test do
    assert_match "hexa #{version}", shell_output("#{bin}/hexa --version")
  end
end
