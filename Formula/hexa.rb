class Hexa < Formula
  desc "Hex editor for the terminal: find bytes, replace, go to, checksums"
  homepage "https://github.com/siriokds/homebrew-tap"
  version "0.2.2"

  depends_on arch: :arm64
  depends_on :macos

  # The program already built: nothing is compiled on install.
  on_macos do
    on_arm do
      url "https://github.com/siriokds/homebrew-tap/releases/download/hexa-#{version}/hexa-#{version}-macos-arm64.tar.gz"
      sha256 "d2eb4622c99d2632788c66373078b74a7410c6aa98d6c503cfb075ec817de218"
    end
  end

  def install
    bin.install "hexa"
  end

  test do
    assert_match "hexa #{version}", shell_output("#{bin}/hexa --version")
  end
end
